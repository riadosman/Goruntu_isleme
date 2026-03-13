import cv2
import time

cap = cv2.VideoCapture(0)

zaman = 0

while True:
    
    sure = time.time() - zaman

    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow(f"{1/sure}", frame)

    # 'q' tuşuna basılırsa döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()