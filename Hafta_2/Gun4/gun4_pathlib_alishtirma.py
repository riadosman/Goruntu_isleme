from pathlib import Path
p = Path("proje/veriler/.gitkeep")
print(p.exists()) # True döner çünkü dosya var. Eğer dosya silinirse False dönecektir.
print(p.parents) # dosyanın bulunduğu klasörleri verir
print(p.name) # dosya adını verir
print(p.suffix) # dosya uzantısını verir
print(p.stem) # dosya adından uzantıyı kaldırır

print(Path("proje/veriler/.gitkeep") / "yeni_dosya.txt") # proje/veriler/.gitkeep/yeni_dosya.txt şeklinde bir yol oluşturur
