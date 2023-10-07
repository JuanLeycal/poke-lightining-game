import Move_class as mv
import Pokemon_cass as pk
import Type_calculator as calculator
import asyncio
import random
import urllib.request
import requests
from io import BytesIO

from tkinter import *
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image

n_moves = []
n_pkmns = []


for i in range(1,901):
    n_moves.append(str(i))
for i in range(1,1005):
    n_pkmns.append(str(i))

x = asyncio.run(mv.get_all(*n_moves))
y = asyncio.run(pk.get_all(*n_pkmns))



def ozuna():
    aux = []
    for i in range(4):
        aux.append(random.randint(1, len(x)))
    
    return aux, random.randint(1, len(y))



    #panel.pack(side="bottom", fill="both", expand="yes")
def Button_Text():
    aux,pkm = ozuna()
    btn1.configure(text=x[aux[0]].name)
    btn2.configure(text=x[aux[1]].name)
    btn3.configure(text=x[aux[2]].name)
    btn4.configure(text=x[aux[3]].name)
    img_url = y[pkm].image
    u = urllib.request.urlopen(img_url)
    raw_data = u.read()
    u.close()
    xd = Image.open(BytesIO(raw_data))
    photo = ImageTk.PhotoImage(xd)
    panel1.configure(image=photo)
    panel1.image = photo


rand, poke = ozuna()

window = tk.Tk()
window.geometry("1280x800")

img_url = y[poke].image
u = urllib.request.urlopen(img_url)
raw_data = u.read()
u.close()
im = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(im)
panel1 = tk.Label(window, image=photo)
panel1.pack(side="top", fill="both", expand="no")

buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
var = 0

btn1 = tk.Button(window, text=x[rand[0]].name, command = Button_Text,height= 4, width=25, font=buttonFont)
btn1.place(relx=0.3, rely=0.65, anchor="center")

btn2 = tk.Button(window, text=x[rand[1]].name, command = Button_Text,height= 4, width=25, font=buttonFont)
btn2.place(relx=0.7, rely=0.65, anchor="center")

btn3 = tk.Button(window, text=x[rand[2]].name, command = Button_Text,height= 4, width=25, font=buttonFont)
btn3.place(relx=0.3, rely=0.85, anchor="center")

btn4 = tk.Button(window, text=x[rand[3]].name, command = Button_Text,height= 4, width=25, font=buttonFont)
btn4.place(relx=0.7, rely=0.85, anchor="center")





window.mainloop()

