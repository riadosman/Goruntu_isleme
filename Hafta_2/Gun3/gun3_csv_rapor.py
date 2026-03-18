import csv
from datetime import datetime
import random
ihlal_turleri = ["goz_kapali", "hareketsiz", "yorgun"]

with open("sahte_veriler.csv", "w" , newline="") as dosya:
  yazici = csv.writer(dosya)
  for i in range(20):
    kayit = []
    kayit.append(f"KID_{random.randint(1, 20)}")
    kayit.append(ihlal_turleri[random.randint(0, len(ihlal_turleri) - 1)])
    kayit.append(round(random.uniform(0, 20), 2))
    kayit.append(round(random.uniform(0, 1), 2)) 
    yazici.writerow(kayit)
    
    

with open("sahte_veriler.csv", "r") as dosya:
    okuyucu = csv.reader(dosya)
    count = 0
    kisi_ihlalleri = {}
    en_uzun_sure = 0
    toplam_ear = 0
    for satir in okuyucu:
        count += 1
        if kisi_ihlalleri.get(satir[0]):
            kisi_ihlalleri[satir[0]] += 1
        else:
            kisi_ihlalleri[satir[0]] = 1
        
        sure = float(satir[2])
        if sure > en_uzun_sure:
            en_uzun_sure = sure

        ear = float(satir[3])
        toplam_ear += ear

    ortalama_ear = toplam_ear / count
    
    for kisi, ihlal_sayisi in kisi_ihlalleri.items():
        print(f"{kisi}: {ihlal_sayisi} ihlal")

    
    print(f"Toplam ihlal sayısı: {count}")
    print(f"En uzun ihlal süresi: {en_uzun_sure}")
    print(f"Ortalama EAR değeri: {ortalama_ear:.3f}")