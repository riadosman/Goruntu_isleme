import argparse
import time
import cv2

parser = argparse.ArgumentParser(description="This is a test for argparse")
parser.add_argument("--kaynak", type=str, help="Video kaynağı")
parser.add_argument("--confidence", type=str, help="Güven eşiği")

args = parser.parse_args()

cap = cv2.VideoCapture(args.kaynak)

frame_count = 0
time_start = time.time()

while True:
    
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)
    frame_count += 1
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
total_time = time.time() - time_start

print(f"Toplam süre: {total_time:.2f} saniye,Frame sayısı: {frame_count}, Ortalama FPS: {frame_count / total_time:.1f} FPS")  