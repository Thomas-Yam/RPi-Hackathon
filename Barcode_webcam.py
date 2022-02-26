import cv2
from pyzbar.pyzbar import decode
import validators
import webbrowser

cap = cv2.VideoCapture(0)

data = None
data0 = None

while True:
    data = None
    
    ret, image = cap.read()
    detectedBarcodes = decode(image)

    for barcode in detectedBarcodes:
        data = barcode.data.decode()       
        print(barcode.data.decode())
        print(barcode.type)

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
            print("data found: ", data)
            data0 = data
            if validators.url(data):
                response = input("Do you want to open the link? (Y, YES): ")
                data0 = None
                if response.upper().strip() == 'Y' or response.upper().strip() == 'YES':
                    webbrowser.open(data, new=2)

cv2.destroyAllWindows()