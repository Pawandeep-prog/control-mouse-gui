import cv2
import numpy as np
import pyautogui
from draw_in_air import draw_in_air
from control_mouse import control_mouse
import tkinter as tk
from PIL import ImageTk, Image
import webbrowser

def callback(url):
    webbrowser.open_new(url)

def manual():
    control_mouse("manual")

def automatic():
    control_mouse("automatic")

root = tk.Tk()

root.geometry("500x400")

image = ImageTk.PhotoImage(Image.open("tap.png"))
img_label = tk.Label(image=image)
img_label.grid(row=0, columnspan=2, pady=10)

label = tk.Label(root, text="Welcome to Virtual Mouse", font='system 18 bold')
label.grid(row=1, columnspan=2, pady=5)

button = tk.Button(root, text="control mouse (Auto)",fg="green", font='TkDefaultFont 12 bold', command=automatic, height="4")
button.grid(row=2, column=0, pady=20, padx=10)


button = tk.Button(root,text="control mouse (Manual)",fg="green", font='TkDefaultFontTkDefaultFont 12 bold', command=manual, height="4")
button.grid(row=2, column=1, pady=20)

button = tk.Button(root,text="Draw in Air",fg="green", font='TkDefaultFont 12 bold', command=draw_in_air, height="4", width="16")
button.grid(row=3, column=0, pady=20)

button = tk.Button(root,text="Close",fg="red", font='TkDefaultFont 12 bold', command=root.quit, height="4", width="16")
button.grid(row=3, column=1, pady=20)

link1 = tk.Label(root, text="How to use?", fg="blue", cursor="hand2", font='TkDefaultFont 12 bold')
link1.grid(row=4, columnspan=2)
link1.bind("<Button-1>", lambda e: callback("about.html"))

root.mainloop()


