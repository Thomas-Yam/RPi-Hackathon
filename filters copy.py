from ast import Invert
import cv2

from PIL import Image
from PIL import ImageTk
import tkinter as tk

import time

import cv2
from picamera2 import *
from null_preview import *


picam2 = Picamera2()
preview = NullPreview(picam2)
picam2.configure(picam2.preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

time.sleep(2)


#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Filters")
window.config(background="#C51A4A")

# Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)


# Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = picam2.capture_array()

def show_frame(initial=False, invert=False, sketch=False, grey=False, outline=True):
    frame = cap
    frame = cv2.flip(frame, 1)
    if initial is True:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    elif invert is True:
        cv2image = cv2.bitwise_not(frame)
    elif sketch is True:
        skgray, cv2image = cv2.pencilSketch(frame, sigma_s=100, sigma_r=0.05, shade_factor=0.075) 
    elif grey is True:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif outline is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        cv2image = cv2.Canny(blurred, 40, 170)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 



def invertFunc():
    a = False
    b = True 
    c = False 
    d = False
    e = False




window.update()
show_frame()


window.mainloop()  # Starts GUI
