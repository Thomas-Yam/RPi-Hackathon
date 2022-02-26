import cv2
from picamera2 import *
from null_preview import *
import webbrowser
import time
import validators

picam2 = Picamera2()
preview = NullPreview(picam2)
picam2.configure(picam2.preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

time.sleep(2)

data_previous = None

# QR code detection object
detector = cv2.QRCodeDetector()


while True:
    # get the image
    img = picam2.capture_array()
    # get bounding box coords and data
    data, bbox, _ = detector.detectAndDecode(img)
    
    # if there is a bounding box, draw one, along with the data
    if(bbox is not None):
        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                     0, 255), thickness=2)
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
        if data:
            if data != data_previous: # check if data is redundant 
                data_previous = data
                print("data found: ", data)
                if validators.url(data):
                    response = input("Do you want to open the link? Y/N: ")
                    if response.upper() == 'Y':
                        webbrowser.open(data, new=2)
    # display the image preview
    cv2.imshow("code detector", img)
    if(cv2.waitKey(1) == ord("q")):
        break
# free camera object and exit
cv2.destroyAllWindows()