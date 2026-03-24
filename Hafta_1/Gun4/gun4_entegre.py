import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from ultralytics import YOLO
import math
import time
from datetime import datetime

# YOLO ve FaceLandmarker
model = YOLO('yolov8n.pt')
options = vision.FaceLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path="C:/Users/Public/face_landmarker.task"),
    running_mode=vision.RunningMode.IMAGE,
    num_faces=1
)
landmarker = vision.FaceLandmarker.create_from_options(options)

def mesafe(p1, p2):
    return math.hypot(p2[0]-p1[0], p2[1]-p1[1])

def ear_hesapla(goz_noktalari):
    p1, p2, p3, p4, p5, p6 = goz_noktalari
    return (mesafe(p2, p6) + mesafe(p3, p5)) / (2 * mesafe(p1, p4))

def id_to_color(id_):
    return ((id_*37)%255, (id_*67)%255, (id_*97)%255)

def tracker_guncelle(tespitler, takip_listesi, sonraki_id, max_mesafe=100):
    yeni_takip = {}
    kullanilan_idler = set()
    for x1, y1, x2, y2 in tespitler:
        cx, cy = int((x1+x2)/2), int((y1+y2)/2)
        en_yakin_id = None
        min_mesafe = float("inf")
        for id_, veri in takip_listesi.items():
            eski_merkez = veri["merkez"]
            d = mesafe(eski_merkez, (cx, cy))
            if d < min_mesafe and d < max_mesafe and id_ not in kullanilan_idler:
                min_mesafe = d
                en_yakin_id = id_
        if en_yakin_id is not None:
            yeni_takip[en_yakin_id] = {"merkez": (cx, cy), "kutu": (x1, y1, x2, y2)}
            kullanilan_idler.add(en_yakin_id)
        else:
            yeni_takip[sonraki_id] = {"merkez": (cx, cy), "kutu": (x1, y1, x2, y2)}
            sonraki_id += 1
    return yeni_takip, sonraki_id

# Video
cap = cv2.VideoCapture(0)
takip_listesi = {}
sonraki_id = 0
kisi_durumlari = {}  # {id: {"goz_baslangic": None, "hareketsiz_baslangic": None}}

HAREKET_ESIK = 20

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO tespiti
    results_yolo = model(frame, conf=0.4, classes=[0])
    tespitler = []
    for det in results_yolo[0].boxes.xyxy:
        x1, y1, x2, y2 = map(int, det)
        tespitler.append((x1, y1, x2, y2))

    # Tracker
    takip_listesi, sonraki_id = tracker_guncelle(tespitler, takip_listesi, sonraki_id)

    for id_, veri in takip_listesi.items():
        x1, y1, x2, y2 = veri["kutu"]
        cx, cy = veri["merkez"]
        renk = id_to_color(id_)

        # Kisi durumu başlat
        if id_ not in kisi_durumlari:
            kisi_durumlari[id_] = {
                "goz_baslangic": None,
                "hareketsiz_baslangic": None
            }

        # --- Hareketsizlik başlangıcı ---
        # Mevcut merkeze göre hareketi kontrol et
        if "onceki_merkez" not in veri:
            veri["onceki_merkez"] = (cx, cy)

        d = mesafe(veri["onceki_merkez"], (cx, cy))
        if d < HAREKET_ESIK and kisi_durumlari[id_]["hareketsiz_baslangic"] is None:
            # Zamanı okunabilir formata kaydet
            kisi_durumlari[id_]["hareketsiz_baslangic"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        veri["onceki_merkez"] = (cx, cy)

        # --- Göz kapanma ---
      # Göz kapanma
    roi_frame = frame[y1:y2, x1:x2]
    if roi_frame.size > 0:
        rgb_frame = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        results_face = landmarker.detect(mp_image)

        if results_face.face_landmarks:
            LEFT_EYE_IDX = [33, 160, 158, 133, 153, 144]
            RIGHT_EYE_IDX = [362, 385, 387, 263, 373, 380]

            left_ear_lms, right_ear_lms = [], []
            for face_landmarks in results_face.face_landmarks:
                for i in LEFT_EYE_IDX:
                    lm = face_landmarks[i]
                    left_ear_lms.append((lm.x, lm.y))
                for i in RIGHT_EYE_IDX:
                    lm = face_landmarks[i]
                    right_ear_lms.append((lm.x, lm.y))

            avg_ear = (ear_hesapla(left_ear_lms) + ear_hesapla(right_ear_lms)) / 2

            # sadece ilk kapanmada zamanı kaydet
            if avg_ear < 0.3 and kisi_durumlari[id_]["goz_baslangic"] is None:
                kisi_durumlari[id_]["goz_baslangic"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # --- Görselleştirme ---
        cv2.rectangle(frame, (x1, y1), (x2, y2), renk, 2)
        cv2.putText(frame, f"ID:{id_}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, renk, 2)

    # Debug: Kisi durumlarini yazdır
    print(kisi_durumlari)

    cv2.imshow("Kamera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
