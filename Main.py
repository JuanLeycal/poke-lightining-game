import Move_class as mv
import Pokemon_cass as pk
import Type_calculator as calc
import asyncio
import random
import urllib.request
from io import BytesIO
from pygame import mixer

from tkinter import *
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image

#GET DATA
n_moves = []
n_pkmns = []


for i in range(1,1000):
    n_moves.append(str(i))
for i in range(1,1010):
    n_pkmns.append(str(i))

x = asyncio.run(mv.get_all(*n_moves))
y = asyncio.run(pk.get_all(*n_pkmns))


#MAIN GUI



def super_effective():
    mixer.init()
    sound = mixer.Sound('sound_effects/sem.mp3')
    sound.set_volume(0.2)
    sound.play()  

def get_moves():
    aux = []
    for i in range(4):
        aux.append(random.randint(1, len(x)))
    
    return aux, random.randint(1, len(y))


rand, poke = get_moves()


def generate_pkm(list_pkm, id):
    url = list_pkm[id].image
    ux = urllib.request.urlopen(url)
    data = ux.read()
    ux.close()
    image = Image.open(BytesIO(data))
    photo = ImageTk.PhotoImage(image)
    return photo

def calculator(attack, defend):
    return calc.type_calculator(attack,defend)

def reroll(one, two, three, four,types_defend):
    boolean = True
    types_attack = [one, two, three,four]
    for i in types_attack:
        if calculator(i,types_defend)>1.0:
            boolean = False
            return boolean
        
    return boolean
            

def action_button1():
    global rand, poke

    if calculator(x[rand[0]].type,y[poke].types)>1.0:
        super_effective()
        print(x[rand[0]].type, y[poke].types)
        aux, pkm = get_moves()
        rand, poke = aux, pkm
        while reroll(x[rand[0]].type,x[rand[1]].type,x[rand[2]].type,x[rand[3]].type,y[poke].types):
            aux, _ = get_moves()
            rand = aux
        btn1.configure(text=x[rand[0]].name)
        btn2.configure(text=x[rand[1]].name)
        btn3.configure(text=x[rand[2]].name)
        btn4.configure(text=x[rand[3]].name)
        p = generate_pkm(y,poke)
        panel1.configure(image=p)
        panel1.image = p
            
    else:
        print("maaaaaal")
        print(x[rand[0]].type, y[poke].types)
    
    

def action_button2():
    global rand, poke
    if calculator(x[rand[1]].type,y[poke].types)>1.0:
        super_effective()
        print(x[rand[1]].type, y[poke].types)
        aux, pkm = get_moves()
        rand, poke = aux, pkm
        while reroll(x[rand[0]].type,x[rand[1]].type,x[rand[2]].type,x[rand[3]].type,y[poke].types):
            aux, _ = get_moves()
            rand = aux
        btn1.configure(text=x[rand[0]].name)
        btn2.configure(text=x[rand[1]].name)
        btn3.configure(text=x[rand[2]].name)
        btn4.configure(text=x[rand[3]].name)
        p = generate_pkm(y,poke)
        panel1.configure(image=p)
        panel1.image = p
        while(reroll(x[rand[0]].type,x[rand[1]].type,x[rand[2]].type,x[rand[3]].type,y[poke].types)):
            action_button2()
    else:
        print("maaaaaal")
        print(x[rand[1]].type, y[poke].types)
    
   

def action_button3():
    global rand, poke
    if calculator(x[rand[2]].type,y[poke].types)>1.0:
        super_effective()
        print(x[rand[2]].type, y[poke].types)
        aux, pkm = get_moves()
        rand, poke = aux, pkm
        while reroll(x[rand[0]].type,x[rand[1]].type,x[rand[2]].type,x[rand[3]].type,y[poke].types):
            aux, _ = get_moves()
            rand = aux
        btn1.configure(text=x[rand[0]].name)
        btn2.configure(text=x[rand[1]].name)
        btn3.configure(text=x[rand[2]].name)
        btn4.configure(text=x[rand[3]].name)
        p = generate_pkm(y,poke)
        panel1.configure(image=p)
        panel1.image = p
        while(reroll(x[rand[0]].type,x[rand[1]].type,x[rand[2]].type,x[rand[3]].type,y[poke].types)):
            action_button3()
    else:
        print("maaaaaal")
        print(x[rand[2]].type, y[poke].types)
    
    
def action_button4():
    global rand, poke
    if calculator(x[rand[3]].type,y[poke].types)>1.0:
        super_effective()
        print(x[rand[3]].type, y[poke].types)
        aux, pkm = get_moves()
        rand, poke = aux, pkm
        while reroll(x[rand[0]].type,x[rand[1]].type,x[rand[2]].type,x[rand[3]].type,y[poke].types):
            aux, _ = get_moves()
            rand = aux
        btn1.configure(text=x[rand[0]].name)
        btn2.configure(text=x[rand[1]].name)
        btn3.configure(text=x[rand[2]].name)
        btn4.configure(text=x[rand[3]].name)
        p = generate_pkm(y,poke)
        panel1.configure(image=p)
        panel1.image = p
        while(reroll(x[rand[0]].type,x[rand[1]].type,x[rand[2]].type,x[rand[3]].type,y[poke].types)):
            action_button3()
    else:
        print("maaaaaal")
        print(x[rand[3]].type, y[poke].types)



window = tk.Tk()
window.geometry("1280x800")


photo = generate_pkm(y,poke)
panel1 = tk.Label(window, image=photo)
panel1.pack(side="top", fill="both", expand="no")

while(reroll(x[rand[0]].type,x[rand[1]].type,x[rand[2]].type,x[rand[3]].type,y[poke].types)):
    rand, _ = get_moves()

buttonFont = font.Font(family='Helvetica', size=16, weight='bold')

btn1 = tk.Button(window, text=x[rand[0]].name, command = action_button1,height= 4, width=25, font=buttonFont)
btn1.place(relx=0.3, rely=0.65, anchor="center")

btn2 = tk.Button(window, text=x[rand[1]].name, command = action_button2,height= 4, width=25, font=buttonFont)
btn2.place(relx=0.7, rely=0.65, anchor="center")

btn3 = tk.Button(window, text=x[rand[2]].name, command = action_button3,height= 4, width=25, font=buttonFont)
btn3.place(relx=0.3, rely=0.85, anchor="center")

btn4 = tk.Button(window, text=x[rand[3]].name, command = action_button4,height= 4, width=25, font=buttonFont)
btn4.place(relx=0.7, rely=0.85, anchor="center")





window.mainloop()

