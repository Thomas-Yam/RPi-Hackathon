import cv2
from pyzbar.pyzbar import decode
 
cap = cv2.VideoCapture(0)
 
ret, image = cap.read()
 
detectedBarcodes = decode(image)
 
for barcode in detectedBarcodes:
     
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)
  
    print(barcode.data)
    print(barcode.type)
 
 
cv2.imshow("Image", image)
  
cv2.waitKey(0)
cv2.destroyAllWindows()