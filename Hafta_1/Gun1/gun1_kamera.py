import cv2

cap = cv2.VideoCapture(0)

while True:
  
    ret, frame = cap.read()
    if not ret:
        break
    (h,w,d) = frame.shape

    cv2.rectangle(frame, (50,50), (150,150), (0,255,0), 2)
    # cv2.rectangle(frame, (x start,x end), (y start,y end), (b, g, r), çizginin kalınlığı)

    cv2.putText(frame, "Gun1", (50, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    # cv2.putText(frame, kelime, (x start, y start), font tipi, büyüklük, renk, kalınlık)

    cv2.circle(frame, (300,300), 50, (255,0,0), 2)
    # cv2.circle(frame, (x start, y start), yarıcap, renk, kalınlık)

    # Renkleri dene: (0, 0, 255) neden kirmizi? (255, 0, 0) neden mavi? BGR mantigini anla.
    # (mavinin şiddeti, yeşilin şiddeti, kırmızının şiddeti)

    cv2.imshow(f"{w}x{h}", frame)
    # 'q' tuşuna basılırsa döngüyü kır
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()