# rehber = {
#   "ALi":"0548648466",
#   "Veli":"0548648467",
# }
# print(rehber["ALi"])
# rehber["Ahmet"] = "0548648468"
# print(rehber)

# rehber["No"]
# Traceback (most recent call last):
#   File "c:\Users\NİTRO\Documents\Goruntu_isleme_adimlarla\odev1_gun0.py", line 9, in <module>
#     rehber["No"]
#     ~~~~~~^^^^^^
# KeyError: 'No'

# .get() metodu ile erişmeye çalışırsak, eğer anahtar yoksa None döner
# print(rehber.get("No"))
# print(rehber.get("No","05*********"))
# print(rehber.get("Ahmet"))

# for isim, numara in rehber.items():
#     print(f"{isim} : {numara}")

# Alistirmalar:

# import time
# import random

# rehber ={}
# rehber["Ayşe"] = "0548648469"
# rehber["Fatma"] = "0548648470"
# rehber["Mehmet"] = "0548648471"
# rehber["Ahmet"] = "0548648468"
# rehber["Veli"] = "0548648467"


# del rehber["Ahmet"]
# print(rehber)

# rehber["Mehmet"] = "0548648472"
# print(rehber)

# for isim, numara in rehber.items():
#     print(f"{isim} : {numara}")

# ogrenciNotlari = {"Ali": [80, 90, 70], "Veli": [60, 85, 75]
#                   , "Ahmet": [50, 80, 65], "Ayşe": [90, 95, 85]
#                   , "Fatma": [70, 75, 80]}

# for isim, notlar in ogrenciNotlari.items():
#     ortalama = sum(notlar) / len(notlar)
#     print(f"{isim} : {ortalama}")

# test1 = "Bu bir test cümlesidir bir başka test cümlesi daha."
# test2 = "Python programlama dili çok popülerdir."


# dict1 = {}

# for kelime in test1.split():
#     test1_sayac = test1.count(kelime)
#     dict1[kelime] = test1_sayac

# print(dict1)
