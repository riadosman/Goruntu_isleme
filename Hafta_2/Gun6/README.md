# 🛡️ GuardWatch V2

**Gerçek zamanlı webcam/video ihlal tespit sistemi**

---

## 🚀 Çalıştırma Modları

### 🎥 Webcam ile Çalıştır

```bash
python guardwatch_v2.py
```

Webcam açılır ve gerçek zamanlı analiz başlar.

---

### 🎬 Video ile Çalıştır

```bash
python guardwatch_v2.py --kaynak test.mp4
```

Verilen video dosyası işlenir.

---

### ❌ Yanlış Dosya Verildiğinde

```bash
python guardwatch_v2.py --kaynak yok.mp4
```

Geçersiz veya bulunamayan dosya için hata mesajı gösterilir.

---

### 📊 CSV Kayıt Modu

```bash
python guardwatch_v2.py --kayit
```

Tespit edilen ihlaller `ihlaller.csv` dosyasına kaydedilir.

---

### 📈 Dashboard

```bash
python dashboard.py
```

Grafikler ve istatistikler oluşturulur.

---

### 🌐 Web Sunucu

```bash
python server.py
```

Sunucu başlar: [http://127.0.0.1:5000/istatistik](http://127.0.0.1:5000/istatistik)

---

### 📡 İstatistik API

Tarayıcıdan `/istatistik` adresine giderek JSON formatında veri alabilirsiniz.

---

## ⚙️ Özellikler

- ✅ Webcam & video desteği
- ✅ Gerçek zamanlı analiz
- ✅ CSV kayıt sistemi
- ✅ Dashboard görselleştirme
- ✅ Web API desteği

---

## 🧠 Proje Yapısı

| Dosya              | Açıklama                |
| ------------------ | ----------------------- |
| `guardwatch_v2.py` | Ana analiz sistemi      |
| `dashboard.py`     | Grafik ve istatistikler |
| `server.py`        | Web API servisi         |
