from flask import Flask, jsonify
import csv
from collections import Counter
app = Flask(__name__)

@app.route("/")
def anasayfa():
    return "<h1>GuardWatch AI Dashboard</h1><p>Sistem calisiyor...</p>"

@app.route("/durum")
def durum():
    return jsonify({
        "sistem": "aktif",
        "toplam_kisi": 5,
        "aktif_ihlal": 2,
        "son_guncelleme": "2026-03-07 14:30:00"
    })


@app.route("/istatistik")
def istatistik():
    kisi_ihlalleri = Counter()
    toplam = 0
    with open("ihlaller.csv", "r") as dosya:
        okuyucu = csv.DictReader(dosya)
        for satir in okuyucu:
            kisi_ihlalleri[satir["kisi_id"]] += 1
            toplam += 1

    en_cok = max(kisi_ihlalleri, key=kisi_ihlalleri.get) if kisi_ihlalleri else "Yok"

    return jsonify({
        "toplam_ihlal": toplam,
        "kisi_sayisi": len(kisi_ihlalleri),
        "en_cok_ihlal": en_cok,
        "kisi_detay": dict(kisi_ihlalleri)
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)

