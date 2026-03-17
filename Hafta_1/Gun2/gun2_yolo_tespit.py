from ultralytics import YOLO
import cv2
# import sys
# print(sys.executable)

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  if not ret:
    break
  results = model(frame, conf=0.4,classes=[0])

  
  for box in results[0].boxes.xyxy:
    kisi_sayisi = len(results[0].boxes)
    x1, y1, x2, y2 = map(int, box)
    cv2.putText(frame, f"Kisi {results[0].boxes.conf[0]*100:.0f}%", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

  cv2.putText(frame, f"Kisi Sayisi {kisi_sayisi}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
  
  cv2.imshow("Kamera", frame)
  # cv2.imshow("Kamera", results[0].boxes.xyxy[0])
  # 'q' tuşuna basılırsa döngüyü kır
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


