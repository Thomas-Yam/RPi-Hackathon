import cv2
from pyzbar.pyzbar import decode
import validators
import webbrowser
from threading import Thread

cap = cv2.VideoCapture(0)

data0 = None
response = None

def cont_to_update():
    if response is None:
        global data
        data = None

        ret, image = cap.read()
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

while True:  
    cont_to_update()

    # check if it is a link
    t = Thread(target=cont_to_update)
    t.start()
    
    if(cv2.waitKey(1) == ord("q")):
        break
    
    if data:
        if data != data0:
            print("data found: ", data)
            data0 = data
            if validators.url(data):
                response = input("Do you want to open the link? Y/N: ")
                data0 = None
                if response.upper().strip() == 'Y' or response.upper().strip() == 'YES':
                    webbrowser.open(data, new=2)

cv2.destroyAllWindows()