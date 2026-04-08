from ultralytics import YOLO
import json
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import time
import pygame

CONFIG_FILE_NAME = "config.json"

takip_listesi = {}
sonraki_id = 0

with open(CONFIG_FILE_NAME, "r") as dosya:
    ayarlar = json.load(dosya)

DURUM_ONCELIK = {
    "NORMAL":     0,
    "HAREKETSIZ": 1,
    "GOZ_KAPALI": 2,
    "UYUYOR":     3,
}

DURUM_RENK = {
    "NORMAL":     (0,   200,   0),
    "HAREKETSIZ": (0,   165, 255),
    "GOZ_KAPALI": (0,   100, 255),
    "UYUYOR":     (0,     0, 255),
}

def set_durum_if_higher(state, new_durum):
    if DURUM_ONCELIK[new_durum] > DURUM_ONCELIK[state["durum"]]:
        state["durum"]      = new_durum
        state["durum_renk"] = DURUM_RENK[new_durum]

def oklid_mesafe(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def merkez_noktasi(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def ear_hesapla(e1, e2):
    p11, p12, p13, p14, p15, p16 = e1
    p21, p22, p23, p24, p25, p26 = e2
    e1_ear = (oklid_mesafe(p12, p16) + oklid_mesafe(p13, p15)) / (2 * oklid_mesafe(p11, p14))
    e2_ear = (oklid_mesafe(p22, p26) + oklid_mesafe(p23, p25)) / (2 * oklid_mesafe(p21, p24))
    return (e1_ear + e2_ear) / 2.0

def id_to_color(id_):
    return (
        (id_ * ayarlar["redcolor_multiplier"])   % ayarlar["color_modulo"],
        (id_ * ayarlar["greencolor_multiplier"]) % ayarlar["color_modulo"],
        (id_ * ayarlar["bluecolor_multiplier"])  % ayarlar["color_modulo"]
    )

def extract_roi(frame, x1, y1, x2, y2, padding=0):
    h_frame, w_frame = frame.shape[:2]
    x1p = max(0,       x1 - padding)
    y1p = max(0,       y1 - padding)
    x2p = min(w_frame, x2 + padding)
    y2p = min(h_frame, y2 + padding)
    if x2p <= x1p or y2p <= y1p:
        return None, (x1p, y1p, x2p, y2p)
    return frame[y1p:y2p, x1p:x2p], (x1p, y1p, x2p, y2p)

model     = YOLO(ayarlar["Yolo_modeli"])
cap       = cv2.VideoCapture(ayarlar["kamera_id"])

pygame.mixer.init()
pygame.mixer.music.load(ayarlar["sound_file"])

options = vision.FaceLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path=ayarlar["face_landmarker_path"]),
    running_mode=vision.RunningMode.IMAGE,
)
landmarker = vision.FaceLandmarker.create_from_options(options)

ROI_PADDING = ayarlar.get("roi_padding", 10)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=ayarlar["yolo_confidence"], classes=[ayarlar["yolo_class_id"]])

    detections = []
    
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            detections.append((x1, y1, x2, y2))

    new_tracks     = {}
    kullanilan_idler = set()

    for det in detections:
        x1, y1, x2, y2 = det
        cx, cy = map(int, merkez_noktasi((x1, y1), (x2, y2)))

        min_mesafe = float("inf")
        matched_id = None

        for id_, state in takip_listesi.items():
            if id_ in kullanilan_idler:
                continue
            mesafe = oklid_mesafe(state["merkez"], (cx, cy))
            if mesafe < min_mesafe and mesafe < ayarlar["tracker_max_mesafe"]:
                min_mesafe = mesafe
                matched_id = id_

        if matched_id is not None:
            kullanilan_idler.add(matched_id)
        else:
            matched_id  = sonraki_id
            sonraki_id += 1

        prev_state = takip_listesi.get(matched_id, {})

        new_tracks[matched_id] = {
            "kutu":             (x1, y1, x2, y2),
            "merkez":           (cx, cy),
            "prev_center":      prev_state.get("merkez", (cx, cy)),
            "eye_closed_start": prev_state.get("eye_closed_start"),
            "not_moving_start": prev_state.get("not_moving_start"),
            "durum":            "NORMAL",
            "durum_renk":       DURUM_RENK["NORMAL"],
        }

    takip_listesi = new_tracks

    for id_, state in takip_listesi.items():

        x1, y1, x2, y2 = state["kutu"]

        roi, (rx1, ry1, rx2, ry2) = extract_roi(frame, x1, y1, x2, y2, padding=ROI_PADDING)
        if roi is None or roi.size == 0:
            continue

        h_roi, w_roi = roi.shape[:2]

        dist = oklid_mesafe(state["prev_center"], state["merkez"])

        if dist < ayarlar["hareket_piksel_esigi"]:
            if state["not_moving_start"] is None:
                state["not_moving_start"] = time.time()
            else:
                elapsed = time.time() - state["not_moving_start"]
                if elapsed >= ayarlar["hareketsizlik_limit_sn"]:
                    set_durum_if_higher(state, "HAREKETSIZ")
        else:
            state["not_moving_start"] = None

        state["prev_center"] = state["merkez"]

        rgb_roi      = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        mp_image     = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_roi)
        face_results = landmarker.detect(mp_image)

        if face_results.face_landmarks:
            for face_landmarks in face_results.face_landmarks:

                left_eye_landmarks  = []
                right_eye_landmarks = []

                for i in ayarlar["LEFT_EYE_IDX"]:
                    lm = face_landmarks[i]
                    left_eye_landmarks.append((int(lm.x * w_roi), int(lm.y * h_roi)))

                for i in ayarlar["RIGHT_EYE_IDX"]:
                    lm = face_landmarks[i]
                    right_eye_landmarks.append((int(lm.x * w_roi), int(lm.y * h_roi)))

                ear_value = ear_hesapla(left_eye_landmarks, right_eye_landmarks)

                if ear_value < ayarlar["ear_threshold"]:
                    if state["eye_closed_start"] is None:
                        state["eye_closed_start"] = time.time()
                    else:
                        eye_elapsed = time.time() - state["eye_closed_start"]

                        if eye_elapsed >= ayarlar["goz_kapali_limit_sn"]:
                            set_durum_if_higher(state, "GOZ_KAPALI")

                            if state["not_moving_start"] is not None:
                                move_elapsed = time.time() - state["not_moving_start"]
                                if move_elapsed >= ayarlar["hareketsizlik_limit_sn"]:
                                    set_durum_if_higher(state, "UYUYOR")
                                    if not pygame.mixer.music.get_busy():
                                        pygame.mixer.music.play()
                else:
                    state["eye_closed_start"] = None

        renk = id_to_color(id_)
        cv2.rectangle(frame, (x1, y1), (x2, y2), renk, 2)
        cv2.putText(frame, f"ID: {id_}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, ayarlar["fontScale"], renk, 2)
        cv2.putText(frame, state["durum"], (x2 - 120, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, ayarlar["fontScale"], state["durum_renk"], 2)

    cv2.imshow("Guard Watch", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 