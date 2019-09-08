from tkinter import *
from PIL import ImageTk,Image
import time as now

root = Tk()

img = ImageTk.PhotoImage(Image.open('card1.png'))

lbl = Label(image=img)
lbl.pack()

time = now.time()

while (now.time()-time)<1 :
    root.update()
