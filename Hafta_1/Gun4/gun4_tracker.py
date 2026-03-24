import cv2
from ultralytics import YOLO
import math
import time

model = YOLO('yolov8n.pt')

def mesafe_hesapla(p1,p2):
    mesafe = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    return mesafe

def select_id(data, key_func):
    return min(data, key=lambda k: key_func(data[k]))

def id_to_color(id_):
    return (
        (id_ * 37) % 255,
        (id_ * 67) % 255,
        (id_ * 97) % 255
    )


cap = cv2.VideoCapture(0)

sonraki_id = 0
takip_listesi = {}  # {id: {"merkez": (cx, cy), "kutu": (x1,y1,x2,y2)}}
def tracker_guncelle(tespitler, takip_listesi, sonraki_id, max_mesafe=100):
    yeni_takip = {}
    kullanilan_idler = set()

    for x1, y1, x2, y2 in tespitler:
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        en_yakin_id = None
        min_mesafe = float("inf")

        # mevcut kişilerle karşılaştır
        for id_, veri in takip_listesi.items():
            eski_merkez = veri["merkez"]
            mesafe = mesafe_hesapla(eski_merkez, (cx, cy))

            if mesafe < min_mesafe and mesafe < max_mesafe:
                min_mesafe = mesafe
                en_yakin_id = id_

        # eşleşme varsa
        if en_yakin_id is not None and en_yakin_id not in kullanilan_idler:
            yeni_takip[en_yakin_id] = {
                "merkez": (cx, cy),
                "kutu": (x1, y1, x2, y2)
            }
            kullanilan_idler.add(en_yakin_id)

        # eşleşme yoksa yeni ID
        else:
            yeni_takip[sonraki_id] = {
                "merkez": (cx, cy),
                "kutu": (x1, y1, x2, y2)
            }
            sonraki_id += 1

    return yeni_takip, sonraki_id


while True:
  ret, frame = cap.read()
  if not ret:
    break

  results = model(frame, conf=0.4,classes=[0])

  listofpersons = []

  for i, box in enumerate(results[0].boxes.xyxy):
    x1, y1, x2, y2 = map(int, box)
    listofpersons.append((x1, y1, x2, y2))
  
  takip_listesi, sonraki_id = tracker_guncelle(
    listofpersons,
    takip_listesi,
    sonraki_id
  )

  for id_, veri in takip_listesi.items():
    x1, y1, x2, y2 = veri["kutu"]
    cx, cy = veri["merkez"]

    renk = id_to_color(id_)

    cv2.rectangle(frame, (x1, y1), (x2, y2), renk, 2)

    cv2.putText(frame, f"ID: {id_}", (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, renk, 2)

    cv2.circle(frame, (cx, cy), 4, renk, -1)



  cv2.imshow("Kamera", frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

    