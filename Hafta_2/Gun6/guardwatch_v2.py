import cv2
import argparse
import csv
from datetime import datetime

parser = argparse.ArgumentParser(description="This is a test for argparse")
parser.add_argument("--kayit",action="store_true", help="Video kaynagini kullan")
parser.add_argument("--kaynak",default=0)

args = parser.parse_args()

def ihlal_kaydet(kisi_id, ihlal_turu, sure, ear):
    """Ihlali CSV dosyasina kaydet"""
    headerler = ["zaman", "kisi_id", "ihlal_turu", "sure", "ear"]
    with open("ihlaller.csv", "a", newline="") as dosya:
        yazici = csv.writer(dosya)
        if dosya.tell() == 0:
            yazici.writerow(headerler)
        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yazici.writerow([zaman, kisi_id, ihlal_turu, sure, f"{ear:.3f}"])

if args.kayit:

  # Kullanim:
  ihlal_kaydet("KID_1", "goz_kapali", 3.5, 0.18)
  ihlal_kaydet("KID_2", "hareketsiz", 12.0, 0.25)
  ihlal_kaydet("KID_3", "goz_kapali", 2.0, 0.15)
  ihlal_kaydet("KID_3", "goz_kapali", 2.0, 0.15)
  ihlal_kaydet("KID_3", "goz_kapali", 2.0, 0.15)
  ihlal_kaydet("KID_3", "goz_kapali", 2.0, 0.15)
  ihlal_kaydet("KID_4", "yorgun", 5.0, 0.20)


cap = cv2.VideoCapture(args.kaynak)

if not cap.isOpened():
    print("Hata: Kaynak açılamadı, webcam deneniyor...")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Hata: Webcam de açılamadı!")
        exit()

while True:
  ret, frame = cap.read()

  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break