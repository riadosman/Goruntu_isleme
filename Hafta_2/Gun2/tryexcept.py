# sayi = input("Bir sayı giriniz: ")

# try:
#     sayi = int(sayi)
#     print("Girdiğiniz sayı:", sayi)
# except ValueError:
#     print("Geçersiz bir sayı girdiniz. Lütfen bir tam sayı giriniz.")


# with open("veriler.txt", "r") as dosya:
#     try:
#         icerik = dosya.read()
#         print("Dosya içeriği:\n", icerik)
#     except FileNotFoundError as e:
#         print("Dosya okunurken bir hata oluştu:", e)


# listem = [1, 2, 3, 4, 5]

# try:
#     print(listem[5])
# except IndexError as e:
#     print("Liste indis hatası:", e)

# mydict = {"a": 1, "b": 2, "c": 3}

# try:
#     print(mydict["d"])
# except KeyError as e:
#     print("Sözlük anahtarı bulunamadı:", e)   
# 
filename = input("Dosya adını giriniz: ")

try:
    with open(filename, "r") as dosya:
        icerik = dosya.read()
        print("Dosya içeriği:\n", icerik)
except FileNotFoundError as e:
    print("Dosya bulunamadı:", e)
else:
    print("Dosya başarıyla okundu. length:", len(icerik))
finally:
    print("Dosya okuma işlemi tamamlandı.")