import cv2
from ultralytics import YOLO
import math
import time

model = YOLO('yolov8n.pt')

def mesafe_hesapla(p1,p2):
    mesafe = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    return mesafe


cap = cv2.VideoCapture(0)
merkez = (None,None)
hareket = True
start = 0

while True:
  ret, frame = cap.read()
  if not ret:
    break
  
  results = model(frame, conf=0.4,classes=[0])

  for box in results[0].boxes.xyxy:
    x1, y1, x2, y2 = map(int, box)
    cx = int((x1+x2)/2)
    cy = int((y1+y2)/2)
    
    if merkez != (None, None):
      mesafe = mesafe_hesapla(merkez,(cx,cy))
      if mesafe < 20:
          if hareket == True:
             start = time.time()
          else:
             sure = time.time() - start
             if sure > 2:
                cv2.putText(frame, "HAREKETSIZ!", (30,30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
          hareket = False
      else:
         hareket = True
    merkez = (cx,cy)


    cv2.putText(frame, f"Kisi {results[0].boxes.conf[0]*100:.0f}%", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

  cv2.imshow("Kamera", frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
