import time
import threading

def islem_1():
  print("Islem 1 basladi")
  time.sleep(2)
  print("Islem 1 bitti")

def islem_2():
  print("Islem 2 basladi")
  time.sleep(4)
  print("Islem 2 bitti")

def islem_3():
  print("Islem 3 basladi")
  time.sleep(1)
  print("Islem 3 bitti")

# zaman = time.time()
# islem_1()
# islem_2()
# islem_3()
# print(f"Toplam sure: {(time.time() - zaman):.0f} saniye")


zaman = time.time()
islem_1_thread = threading.Thread(target=islem_1)
islem_2_thread = threading.Thread(target=islem_2)
islem_3_thread = threading.Thread(target=islem_3)

islem_1_thread.start()
islem_2_thread.start()
islem_3_thread.start()

islem_1_thread.join()
islem_2_thread.join()
islem_3_thread.join()
print(f"Toplam sure: {(time.time() - zaman):.0f} saniye")

