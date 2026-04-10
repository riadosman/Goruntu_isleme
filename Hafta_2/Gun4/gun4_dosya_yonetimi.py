import os
from datetime import datetime
import time
import random
import csv

if not os.path.exists("kayitlar"):
    os.mkdir("kayitlar")

with open("kayitlar/ihlaller.csv", "a", newline="") as dosya:
    titles = ["Zaman", "KisiID", "IhlalTuru", "Sure", "EAR", "FrameYolu"]
    if os.stat("kayitlar/ihlaller.csv").st_size == 0:
      yazici = csv.DictWriter(dosya, fieldnames=titles)
      yazici.writeheader()
    else:
      yazici = csv.DictWriter(dosya, fieldnames=titles)

    for i in range(5):
        zaman = datetime.now().strftime("%Y-%m-%d")
        kisi_id = random.randint(1000, 9999)
        ihlal_turu = random.choice(["Yorgun", "Hareketsiz", "Kirmizi İsik"])
        sure_sn = random.randint(1, 10)
        ear_degeri = round(random.uniform(0.1, 1.0), 3)
        frame_yolu = os.path.join("kayitlar", zaman, f"ihlal_{kisi_id}_{ihlal_turu}.jpg")
        yazici.writerow({
            "Zaman": zaman,
            "KisiID": kisi_id,
            "IhlalTuru": ihlal_turu,
            "Sure": sure_sn,
            "EAR": ear_degeri,
            "FrameYolu": frame_yolu
        })
        time.sleep(1)
        if not os.path.exists(os.path.join("kayitlar", zaman)):
            os.makedirs(os.path.join("kayitlar", zaman))

        with open(os.path.abspath(frame_yolu), "w") as frame_dosyasi:
            pass

with open("kayitlar/ihlaller.csv") as f:
    count = 0
    toplam = 0
    tarihler = {}
    ihlal_turu = {}
    okuyucu = csv.DictReader(f)
    for satir in okuyucu:
        count += 1
        toplam += int(satir["Sure"])
        if tarihler.get(satir["Zaman"]):
            tarihler[satir["Zaman"]] += 1
        else:
            tarihler[satir["Zaman"]] = 1

        if ihlal_turu.get(satir["IhlalTuru"]):
            ihlal_turu[satir["IhlalTuru"]] += 1
        else:
            ihlal_turu[satir["IhlalTuru"]] = 1

    print(f"Toplam ihlal sayısı: {count}")
    print(f"Ortalama ihlal suresi: {(toplam / count):.2f}")

    for tarih, ihlal_sayisi in tarihler.items():
        print(f"{tarih}: {ihlal_sayisi} ihlal")

    for ihlal_turu, ihlal_sayisi in ihlal_turu.items():
        print(f"{ihlal_turu}: {ihlal_sayisi} ihlal")

print(os.listdir("kayitlar"))