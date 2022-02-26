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

# QR code detection object
detector = cv2.QRCodeDetector()

data0 = None

while True:
    # get the image
    frame = picam2.capture_array()
    
    # Normal
    #cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

    # Invert
    #cv2image = cv2.bitwise_not(frame)

    # Sketch
    skgray, cv2image = cv2.pencilSketch(frame, sigma_s=100, sigma_r=0.05, shade_factor=0.075) 

    # Grey
    #cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Outline
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    #cv2image = cv2.Canny(blurred, 40, 170)

    # display the image preview
    cv2.imshow("Filter", cv2image)
    if(cv2.waitKey(1) == ord("q")):
        break
# free camera object and exit
cv2.destroyAllWindows()