from ast import Invert
import cv2

from PIL import Image
from PIL import ImageTk
import tkinter as tk

import time


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
cap = cv2.VideoCapture(0)

def show_frame(initial=False, invert=False, sketch=False, grey=True, outline=False):
    _, frame = cap.read()
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


def pencilFunc():
    a = False
    b = False
    c = True 
    d = False
    e = False
    

def greyFunc():
    a = False
    b = False
    c = False 
    d = True
    e = False
    

def outlineFunc():
    a = False
    b = False
    c = False 
    d = False
    e = True
    


# Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)

invertButton = tk.Button(sliderFrame, text="Invert", command=invertFunc)
invertButton.pack(side=tk.LEFT)

greyButton = tk.Button(sliderFrame, text="Grey", command=greyFunc)
greyButton.pack(side=tk.LEFT)

pencilButton = tk.Button(sliderFrame, text="Sketch", command=pencilFunc)
pencilButton.pack(side=tk.LEFT)

outlineButton = tk.Button(sliderFrame, text="Outline", command=outlineFunc)
outlineButton.pack(side=tk.LEFT)

a = True
b = False
c = False 
d = False
e = False

window.update()
show_frame(a, b, c, d, e)

while True:
    time.sleep(1)
    show_frame(a, b, c, d, e)  # Display 2

window.mainloop()  # Starts GUI
