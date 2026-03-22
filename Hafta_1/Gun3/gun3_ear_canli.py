import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import math

cap = cv2.VideoCapture(0)

options = vision.FaceLandmarkerOptions(
   base_options = python.BaseOptions(model_asset_path="C:/Users/Public/face_landmarker.task"),
   running_mode = vision.RunningMode.IMAGE,
   num_faces=1
)
landmarker = vision.FaceLandmarker.create_from_options(options)

def oklid_mesagfe(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    mesafe = math.sqrt(math.pow(abs(x1 - x2),2) + math.pow(abs(y1 - y2),2))
    return mesafe

def ear_hesapla(goz_noktalari):
    p1,p2,p3,p4,p5,p6 = goz_noktalari
    mesafe = (oklid_mesagfe(p2,p6) + oklid_mesagfe(p3,p5)) / (2 * oklid_mesagfe(p1,p4))
    return mesafe
    
while cap.isOpened():
  ret, frame = cap.read()
  if not ret:
      break
  
  rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
  mp_image = mp.Image(image_format=mp.ImageFormat.SRGB,data=rgb_frame)
  results = landmarker.detect(mp_image)
  height, width,_ = frame.shape

  if results.face_landmarks:
        LEFT_EYE_IDX = [33, 160, 158, 133, 153, 144]  
        RIGHT_EYE_IDX = [362, 385, 387, 263, 373, 380]
        left_ear_lms = []
        right_ear_lm = []

        for face_landmarks in results.face_landmarks:
          for i in LEFT_EYE_IDX:
              lm = face_landmarks[i] 
              mx,my = lm.x,lm.y
              left_ear_lms.append((mx,my))
              x = int(lm.x * width)
              y = int(lm.y * height)
              cv2.circle(frame, (x, y), 3, (0, 0, 255), -1) 
          

          for i in RIGHT_EYE_IDX:
              lm = face_landmarks[i]
              mx,my = lm.x,lm.y
              right_ear_lm.append((mx,my))
              x = int(lm.x * width)
              y = int(lm.y * height)
              cv2.circle(frame, (x, y), 3, (255, 0, 0), -1) 

        left_ear_value = ear_hesapla(left_ear_lms)
        right_ear_value = ear_hesapla(right_ear_lm)
        avg_ear = (left_ear_value + right_ear_value) / 2

        cv2.putText(frame, f"Left EAR: {left_ear_value:.2f}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        cv2.putText(frame, f"Right EAR: {right_ear_value:.2f}", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
        cv2.putText(frame, f"Avg EAR: {avg_ear:.2f}", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)


        print(f"Sol EAR {ear_hesapla(left_ear_lms)}")
        print(f"SAG EAR {ear_hesapla(right_ear_lm)}")
        print(f"Ortalama EAR {(ear_hesapla(right_ear_lm) + ear_hesapla(left_ear_lms)) / 2}")
        

  cv2.imshow("FaceMash_Ear_Canli",frame)

  if cv2.waitKey(1) & 0xFF == ord("q"):
     break

cap.release()
cv2.destroyAllWindows()