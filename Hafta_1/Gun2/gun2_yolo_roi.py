from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)

ret,frame = cap.read()
  
x, y, w, h = cv2.selectROI("Goruntu", frame, False, False)

print(f"ROI Koordinatları: x={x}, y={y}, w={w}, h={h}")


def merkez_bolgede_mi(kutu, bolge):
  if kutu[0] < bolge[0] + bolge[2] and kutu[0] > bolge[0] and kutu[1] < bolge[1] + bolge[3] and kutu[1] > bolge[1]:
    return True
  return False

while True:

  ret,frame = cap.read()

  if not ret:
    break

  results = model(frame, conf=0.4,classes=[0])

  for box in results[0].boxes.xyxy:
    x1, y1, x2, y2 = map(int, box)
    xcenter = (x1 + x2) // 2
    ycenter = (y1 + y2) // 2

    if merkez_bolgede_mi([xcenter, ycenter], [x, y, w, h]):
      cv2.putText(frame, f"Kisi {results[0].boxes.conf[0]*100:.0f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
      cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

  cv2.imshow("Kamera", frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()