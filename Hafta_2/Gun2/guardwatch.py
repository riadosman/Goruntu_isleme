import os
import cv2
import sys
import json
from ultralytics import YOLO

kaynak = input("Video kaynağını giriniz: ")
cap = cv2.VideoCapture(kaynak)

cap = cv2.VideoCapture(kaynak)
if not cap.isOpened():
    print(f"HATA: '{kaynak}' acilamadi!")
    print("Webcam icin 0, video icin dosya yolunu kontrol et.")
    sys.exit(1)


try:
    model = YOLO("yolov8n.pt")
except Exception as e:
    print(f"HATA: YOLO modeli yuklenemedi: {e}")
    print("'yolov8n.pt' dosyasinin var oldugundan emin ol.")
    sys.exit(1)


try:
    with open("config.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    print("UYARI: config.json bulunamadi, varsayilan degerler kullaniliyor")
    config = {"ear_esik": 0.22, "sure_esik": 2.0}
except json.JSONDecodeError:
    print("UYARI: config.json bozuk, varsayilan degerler kullaniliyor")
    config = {"ear_esik": 0.22, "sure_esik": 2.0}

if kaynak != "0" and not os.path.exists(kaynak):
    print(f"HATA: Video dosyasi bulunamadi: '{kaynak}'")
    sys.exit(1)