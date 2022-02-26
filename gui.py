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

def initialFunc():
    imageFrame.destroy()
    

    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, initialFunc) 

def invertFunc():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.bitwise_not(frame)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, invertFunc) 

def pencilFunc():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    skgray, cv2image = cv2.pencilSketch(frame, sigma_s=100, sigma_r=0.05, shade_factor=0.075) 
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, pencilFunc) 

def greyFunc():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, greyFunc) 

def outlineFunc():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2image = cv2.Canny(blurred, 40, 170)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, outlineFunc) 

# Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)

originalButton = tk.Button(sliderFrame, text="Invert", command=initialFunc)
originalButton.pack(side=tk.LEFT)

invertButton = tk.Button(sliderFrame, text="Invert", command=invertFunc)
invertButton.pack(side=tk.LEFT)

greyButton = tk.Button(sliderFrame, text="Grey", command=greyFunc)
greyButton.pack(side=tk.LEFT)

pencilButton = tk.Button(sliderFrame, text="Sketch", command=pencilFunc)
pencilButton.pack(side=tk.LEFT)

outlineButton = tk.Button(sliderFrame, text="Outline", command=outlineFunc)
outlineButton.pack(side=tk.LEFT)



window.update()
initialFunc()

while True:
    window.update()

window.mainloop()  # Starts GUI
