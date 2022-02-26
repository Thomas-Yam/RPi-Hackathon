import cv2
from picamera2 import *
from null_preview import *
import webbrowser
import time
import validators
from pyzbar.pyzbar import decode

picam2 = Picamera2()
preview = NullPreview(picam2)
picam2.configure(picam2.preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

time.sleep(2)

# QR code detection object
detector = cv2.QRCodeDetector()

data0 = None

while True:
    # get the image
    img = picam2.capture_array()

    detectedBarcodes = decode(img)
    
    for barcode in detectedBarcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
        print(barcode.data)
        print(barcode.type)
            
    # display the image preview
    cv2.imshow("code detector", img)
    if(cv2.waitKey(1) == ord("q")):
        break
    
# free camera object and exit
cv2.destroyAllWindows()