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

data = None
data0 = None

while True:
    data = None  

    # get the image
    image = picam2.capture_array()
    detectedBarcodes = decode(image)

    for barcode in detectedBarcodes:
        data = barcode.data.decode()

        # check if it is a QR code
        if barcode.type == 'QRCODE':
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
            cv2.putText(image, barcode.data.decode(), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

        else:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 5)
            cv2.putText(image, barcode.data.decode(), (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2) 
    
    cv2.imshow("Video",image)

    if(cv2.waitKey(1) == ord("q")):
        break
    
    # check if it is a link
    if data:
        if data != data0:
            print("Data found: ", data)
            print("Data type: ", barcode.type)
            data0 = data
            if validators.url(data):
                response = input("Do you want to open the link? (Y, YES): ")
                data0 = None
                if response.upper().strip() == 'Y' or response.upper().strip() == 'YES':
                    webbrowser.open(data, new=2)

cv2.destroyAllWindows()