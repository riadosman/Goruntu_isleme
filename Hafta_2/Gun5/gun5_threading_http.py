import requests
import threading
import time
def guvenli_istek(url, timeout=5):
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
  
def islem_1():
  zaman = time.time()
  veri = guvenli_istek("https://api.ipify.org?format=json")
  sure = time.time() - zaman
  print(f"IP sure: {sure} saniye")

def islem_2():
  zaman = time.time()
  veri = guvenli_istek("https://www.boredapi.com/api/activity")
  sure = time.time() - zaman
  print(f"Rastgele aktivite sure: {sure} saniye")

def islem_3():
  zaman = time.time()
  veri = guvenli_istek("https://official-joke-api.appspot.com/random_joke")
  sure = time.time() - zaman
  print(f"Rastgele joke sure: {sure} saniye")

zaman = time.time()
islem_1_thread = threading.Thread(target=islem_1)
islem_2_thread = threading.Thread(target=islem_2)
islem_3_thread = threading.Thread(target=islem_3)

islem_2_thread.start()
islem_1_thread.start()
islem_3_thread.start()

islem_2_thread.join()
islem_1_thread.join()
islem_3_thread.join()

print(f"Toplam sure: {(time.time() - zaman):.0f} saniye")