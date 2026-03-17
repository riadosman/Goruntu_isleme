import random
import math
import time

nesneler = {"Araba": (100, 200), "Kisi": (300, 150), "Top": (50, 50)}

def mesafe_hesapla(p1,p2):
    mesafe = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    return mesafe


for i in range(10):
    for nesne, koordinat in nesneler.items():
      hareketX = random.randint(-30,30)
      hareketY = random.randint(-30,30)
      yeniKoordinat = (koordinat[0] + hareketX, koordinat[1] + hareketY)
      toplamHareket = mesafe_hesapla(koordinat, yeniKoordinat)
      koordinat = yeniKoordinat
      if toplamHareket < 10:
        print("HAREKETSIZ")
      else:
        print("HAREKET EDIYOR")

      print(f"{nesne} nesnesi {koordinat} koordinatindan {yeniKoordinat} koordinatina hareket etti.")
    time.sleep(1)