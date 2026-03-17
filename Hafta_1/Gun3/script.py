import cv2
from mediapipe.tasks import python
from mediapipe.tasks.python.vision import face_landmarker
from mediapipe.tasks.python.vision import vision

# ---- initialize ----
options = face_landmarker.FaceLandmarkerOptions(
    model_path="mediapipe/tasks/face_landmarker/face_landmarker_full.task",
    num_faces=1
)
landmarker = face_landmarker.FaceLandmarker.create_from_options(options)

# Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = vision.Image.create_from_array(rgb_frame)

    results = landmarker.detect(mp_image)

    height, width, _ = frame.shape

    for face in results.faces:
        for lm in face.landmarks:
            x = int(lm.x * width)
            y = int(lm.y * height)
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

    cv2.imshow("FaceMesh", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
