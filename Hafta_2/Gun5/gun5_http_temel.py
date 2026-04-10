# import requests

# # Basit GET istegi
# response = requests.get("https://httpbin.org/get")
# print(f"Status: {response.status_code}")  # 200
# print(f"JSON: {response.json()}")

# # Public API ornegi - IP bilgisi
# response = requests.get("https://api.ipify.org?format=json")
# veri = response.json()
# print(f"IP adresin: {veri['ip']}")



import requests

def guvenli_istek(url, timeout=5):
    """HTTP istegi yap, hata olursa None don"""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # 4xx/5xx ise hata firlat
        return response.json()
    except requests.exceptions.Timeout:
        print(f"UYARI: {url} zaman asimi!")
        return None
    except requests.exceptions.ConnectionError:
        print(f"UYARI: {url} baglanti hatasi!")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"UYARI: HTTP hatasi: {e}")
        return None

# Kullanim:
veri = guvenli_istek("https://api.ipify.org?format=json")
if veri:
    print(f"IP: {veri['ip']}")
else:
    print("Veri alinamadi!")