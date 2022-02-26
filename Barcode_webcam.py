import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()

    cv2.imshow("hi",image)
    detectedBarcodes = decode(image)
    for barcode in detectedBarcodes:
     
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)
    
        print(barcode.data)
        print(barcode.type)

    if(cv2.waitKey(1) == ord("q")):
        break

cv2.destroyAllWindows()