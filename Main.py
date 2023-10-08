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

#GET DATA
n_moves = []
n_pkmns = []


for i in range(1,901):
    n_moves.append(str(i))
for i in range(1,1005):
    n_pkmns.append(str(i))

x = asyncio.run(mv.get_all(*n_moves))
y = asyncio.run(pk.get_all(*n_pkmns))



#MAIN GUI

def get_moves():
    aux = []
    for i in range(4):
        aux.append(random.randint(1, len(x)))
    
    return aux, random.randint(1, len(y))

def generate_pkm(list_pkm, id):
    url = list_pkm[id].image
    ux = urllib.request.urlopen(url)
    data = ux.read()
    ux.close()
    image = Image.open(BytesIO(data))
    photo = ImageTk.PhotoImage(image)
    return photo


def Button_Text():
    aux,pkm = get_moves()
    btn1.configure(text=x[aux[0]].name)
    btn2.configure(text=x[aux[1]].name)
    btn3.configure(text=x[aux[2]].name)
    btn4.configure(text=x[aux[3]].name)
    p = generate_pkm(y,pkm)
    panel1.configure(image=p)
    panel1.image = p


rand, poke = get_moves()

window = tk.Tk()
window.geometry("1280x800")


photo = generate_pkm(y,poke)
panel1 = tk.Label(window, image=photo)
panel1.pack(side="top", fill="both", expand="no")

buttonFont = font.Font(family='Helvetica', size=16, weight='bold')

btn1 = tk.Button(window, text=x[rand[0]].name, command = Button_Text,height= 4, width=25, font=buttonFont)
btn1.place(relx=0.3, rely=0.65, anchor="center")

btn2 = tk.Button(window, text=x[rand[1]].name, command = Button_Text,height= 4, width=25, font=buttonFont)
btn2.place(relx=0.7, rely=0.65, anchor="center")

btn3 = tk.Button(window, text=x[rand[2]].name, command = Button_Text,height= 4, width=25, font=buttonFont)
btn3.place(relx=0.3, rely=0.85, anchor="center")

btn4 = tk.Button(window, text=x[rand[3]].name, command = Button_Text,height= 4, width=25, font=buttonFont)
btn4.place(relx=0.7, rely=0.85, anchor="center")





window.mainloop()

