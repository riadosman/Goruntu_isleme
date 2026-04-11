# import matplotlib.pyplot as plt

# # Bar chart: Kisi bazli ihlal sayisi
# kisiler = ["KID_1", "KID_2", "KID_3", "KID_4"]
# ihlaller = [5, 12, 3, 8]

# plt.figure(figsize=(8, 5))
# plt.bar(kisiler, ihlaller, color="steelblue")
# plt.title("Kisi Bazli Ihlal Sayisi")
# plt.xlabel("Kisi ID")
# plt.ylabel("Ihlal Sayisi")
# plt.savefig("ihlal_grafik.png", dpi=150, bbox_inches="tight")
# plt.close()
# print("Grafik kaydedildi: ihlal_grafik.png")


# saatler = list(range(8, 18))  # 08:00 - 17:00
# ihlal_sayilari = [2, 5, 3, 1, 8, 12, 6, 4, 9, 7]

# plt.figure(figsize=(10, 5))
# plt.plot(saatler, ihlal_sayilari, marker="o", color="crimson", linewidth=2)
# plt.title("Saatlik Ihlal Dagilimi")
# plt.xlabel("Saat")
# plt.ylabel("Ihlal Sayisi")
# plt.grid(True, alpha=0.3)
# plt.savefig("saatlik_ihlal.png", dpi=150, bbox_inches="tight")
# plt.close()

# import csv
# import matplotlib.pyplot as plt

# with open("veri.csv", "r") as file:
#   reader = csv.reader(file)
#   next(reader)  # Skip the header row

#   isimler = []
#   notlar = []

#   for row in reader:
#       isimler.append(row[0])
#       notlar.append(int(row[1]))

#   plt.figure(figsize=(10, 5))
#   plt.bar(isimler, notlar, color="steelblue")
#   plt.title("Ogrenci Notlari")
#   plt.xlabel("Ogrenci Isimleri")
#   plt.ylabel("Notlar")
#   plt.savefig("not_grafik.png", dpi=150, bbox_inches="tight")
#   plt.close()


#   plt.plot(isimler, notlar, marker="o", color="crimson", linewidth=2)
#   plt.title("Ogrenci Notlari")
#   plt.xlabel("Ogrenci Isimleri")
#   plt.ylabel("Notlar")
#   plt.grid(True, alpha=0.3)
#   plt.savefig("not_plot.png", dpi=150, bbox_inches="tight")
#   plt.close()

import csv
import matplotlib.pyplot as plt
from collections import Counter

# CSV'den veri oku
kisi_ihlalleri = Counter()
with open("ihlaller.csv", "r") as dosya:
    okuyucu = csv.DictReader(dosya)
    for satir in okuyucu:
        kisi_ihlalleri[satir["kisi_id"]] += 1

# Bar chart
kisiler = list(kisi_ihlalleri.keys())
sayilar = list(kisi_ihlalleri.values())

plt.figure(figsize=(8, 5))
plt.bar(kisiler, sayilar, color="steelblue")
plt.title("Kisi Bazli Ihlal Sayisi")
plt.xlabel("Kisi ID")
plt.ylabel("Ihlal Sayisi")
plt.savefig("dashboard_kisi.png", dpi=150, bbox_inches="tight")
plt.close()
print("Dashboard grafigi kaydedildi!")