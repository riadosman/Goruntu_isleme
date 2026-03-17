import math

def mesafe_hesapla(p1,p2):
    mesafe = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    return mesafe

nokta = input("Bir nokta giriniz (x,y): ")

hedefNoktalar = [(0,5), (8,0), (9,-5), (-8,9)]

print(f"Girdiginiz nokta: ({nokta.split(',')[0]}, {nokta.split(',')[1]})")

minMesafe = 0

enYakinNokta = ""

for hedef in hedefNoktalar:
    if minMesafe == 0:
        minMesafe = mesafe_hesapla((float(nokta.split(',')[0]), float(nokta.split(',')[1])), hedef)
        enYakinNokta = hedef
    if minMesafe > mesafe_hesapla((float(nokta.split(',')[0]), float(nokta.split(',')[1])), hedef):
        minMesafe = mesafe_hesapla((float(nokta.split(',')[0]), float(nokta.split(',')[1])), hedef)
        enYakinNokta = hedef


print(f"En yakin nokta: {enYakinNokta} | Mesafe: {minMesafe:.2f}")