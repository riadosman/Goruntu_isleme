from ultralytics import YOLO
import cv2
import random

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)

while True:
  ret,frame = cap.read()

  if not ret:
    break

  results = model(frame, conf=0.4,classes=[0])

  for box in results[0].boxes.xyxy:
    kisiSayisi = len(results[0].boxes)
    print(f"Kisi Sayisi: {kisiSayisi}")
    renkler = []
    for index in range(kisiSayisi):
      blue = random.randint(0, 255)
      green = random.randint(0, 255)
      red = random.randint(0, 255)
      renkler.append((blue, green, red))
      x1, y1, x2, y2 = map(int, box)
      cv2.putText(frame, f"Kisi {results[index].boxes.conf[0]*100:.0f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, renkler[index], 2)
      cv2.rectangle(frame, (x1, y1), (x2, y2), renkler[index], 2)

  # Burada bir PROBLEM fark edeceksin: YOLO her frame'de tespitleri SIFIRDAN yapiyor. Yani frame 1'de "1. kisi" olan, frame 2'de "2. kisi" olabiliyor. Renkler surekli degisiyor. Bu problemi YAZI ILE NOT ET. Cunku Gun 4'te bunu cozeceksin.

  cv2.imshow("Kamera", frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
