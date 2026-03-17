import argparse

parser = argparse.ArgumentParser(description="This is a test for argparse")

parser.add_argument("--isim", type=str, help="Isminizi giriniz")
parser.add_argument("--yas", type=int, help="Yasinizi giriniz")
parser.add_argument("--ogrenci", action="store_true", help="Bekar misiniz?")

args = parser.parse_args()

print(f"Isim: {args.isim}")
print(f"Yas: {args.yas}")
print(f"Ogrenci: {args.ogrenci}")