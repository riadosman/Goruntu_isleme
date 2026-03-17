import cv2
import argparse
import time

args = argparse.ArgumentParser(description="Video kaynağı seçimi")
args.add_argument("--kaynak", type=str, default="0", help="Video kaynağı (0: webcam, dosya yolu)")
args = args.parse_args()

if args.kaynak == "0": 
    cap = cv2.VideoCapture(0) 
else: 
    cap = cv2.VideoCapture(args.kaynak) 

time_start = time.time()
frame_count = 0

while True:
    frame_start = time.time()
    ret, frame = cap.read()

    if not ret:
        break
          # cap.get(cv2.CAP_PROP_FPS)
    
    frame_time = time.time() - frame_start
    frame_count += 1

    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"FPS: {fps}")


    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

total_time = time.time() - time_start

print(f"Toplam süre: {total_time:.2f} saniye,Frame sayısı: {frame_count}, Ortalama FPS: {frame_count / total_time:.1f} FPS")

cap.release()
cv2.destroyAllWindows()