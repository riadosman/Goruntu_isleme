# import csv

# # Yeni CSV dosyasi olustur
# with open("ogrenciler.csv", "w", newline="") as dosya:
#     yazici = csv.writer(dosya)
#     yazici.writerow(["isim", "yas", "not"])  # Baslik satiri
#     yazici.writerow(["Taha", 23, 85])
#     yazici.writerow(["Ali", 25, 72])
#     yazici.writerow(["Ayse", 22, 95])

# print("CSV dosyasi olusturuldu!")


# import csv

# basliklar = ["isim", "yas", "not"]

# with open("ogrenciler2.csv", "w", newline="") as dosya:
#     yazici = csv.DictWriter(dosya, fieldnames=basliklar)
#     yazici.writeheader()
#     yazici.writerow({"isim": "Taha", "yas": 23, "not": 85})
#     yazici.writerow({"isim": "Ali", "yas": 25, "not": 72})

# import csv

# csv.reader ile okuma
# with open("ogrenciler.csv", "r") as dosya:
#     okuyucu = csv.reader(dosya)
#     basliklar = next(okuyucu)  # Ilk satir baslik
#     for satir in okuyucu:
#         print(f"Isim: {satir[0]}, Yas: {satir[1]}, Not: {satir[2]}")

# csv.DictReader ile okuma (daha okunakli)
# with open("ogrenciler.csv", "r") as dosya:
#     okuyucu = csv.DictReader(dosya)
#     for satir in okuyucu:
#         print(f"Isim: {satir['isim']}, Not: {satir['not']}")

# with open("veri.csv", "r") as dosya:
#     okuyucu = csv.DictReader(dosya)
#     total = 0
#     count = 0
#     for satir in okuyucu: # bir defa kullanilmali cunku okuyucu iteratorudur, ikinci defa kullanilmaz
#         total += int(satir["not"])
#         count += 1
#         try:
#           ortalama = total / count
#         except ZeroDivisionError:
#             print("Veri bulunamadı, ortalama hesaplanamıyor.")
#         if int(satir["not"]) > ortalama:
#             print(f"{satir['isim']} ortalamanın üzerinde not aldı: {satir['not']}")
      
import csv
from datetime import datetime

def ihlal_kaydet(kisi_id, ihlal_turu, sure, ear):
    """Ihlali CSV dosyasina kaydet"""
    headerler = ["zaman", "kisi_id", "ihlal_turu", "sure", "ear"]
    with open("ihlaller.csv", "a", newline="") as dosya:
        yazici = csv.writer(dosya)
        if dosya.tell() == 0:
            yazici.writerow(headerler)
        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yazici.writerow([zaman, kisi_id, ihlal_turu, sure, f"{ear:.3f}"])

# Kullanim:
ihlal_kaydet("KID_1", "goz_kapali", 3.5, 0.18)
ihlal_kaydet("KID_2", "hareketsiz", 12.0, 0.25)
ihlal_kaydet("KID_3", "goz_kapali", 2.0, 0.15)
ihlal_kaydet("KID_3", "goz_kapali", 2.0, 0.15)
ihlal_kaydet("KID_3", "goz_kapali", 2.0, 0.15)
ihlal_kaydet("KID_3", "goz_kapali", 2.0, 0.15)
ihlal_kaydet("KID_4", "yorgun", 5.0, 0.20)

# import time
# from datetime import datetime

# # Unix timestamp
# ts = time.time()
# print(f"Unix timestamp: {ts}")  # 1741089600.123

# # Okunabilir format
# okunabilir = datetime.fromtimestamp(ts)
# print(f"Okunabilir: {okunabilir}")  # 2026-03-04 14:30:00.123

# # Formatli string
# formatli = okunabilir.strftime("%Y-%m-%d %H:%M:%S")
# print(f"Formatli: {formatli}")  # 2026-03-04 14:30:00


from datetime import datetime
import time
import csv

# for i in range(10):
#   time.sleep(1)  # 1 saniye bekle
#   with open("zaman.csv", "a", newline="") as dosya:
#     yazici = csv.writer(dosya)
#     zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     yazici.writerow([zaman])

with open("zaman.csv", "r") as dosya:
    okuyucu = csv.reader(dosya)
    count = 0
    for i, satir in enumerate(okuyucu, start=1):
      count += 1
      print(f"{i}. ihlal zamanı: {satir[0]}")

    print(f"Toplam ihlal sayısı: {count}")