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

# ==== CARGA DE DATOS ====

all_moves = asyncio.run(mv.get_all(*map(str, range(928))))
all_pokemon = asyncio.run(pk.get_all(*map(str, range(1026))))

# ==== FUNCIONES DE UTILIDAD ====

def super_effective():
    mixer.init()
    sound = mixer.Sound('sound_effects/sem.mp3')
    sound.set_volume(0.2)
    sound.play()

def get_new_round():
    moves = random.sample(range(len(all_moves)), 4)
    pkmn = random.randint(0, len(all_pokemon) - 1)
    return moves, pkmn

def generate_pkm_image(pkmn_obj):
    url = pkmn_obj.image
    with urllib.request.urlopen(url) as ux:
        data = ux.read()
    image = Image.open(BytesIO(data))
    return ImageTk.PhotoImage(image)

def is_super_effective(move_type, target_types):
    return calc.type_calculator(move_type, target_types) > 1.0

def is_valid_round(move_types, target_types):
    return any(is_super_effective(t, target_types) for t in move_types)

# ==== FUNCIONES DE JUEGO ====

def update_ui():
    btn1.configure(text=all_moves[move_indices[0]].name)
    btn2.configure(text=all_moves[move_indices[1]].name)
    btn3.configure(text=all_moves[move_indices[2]].name)
    btn4.configure(text=all_moves[move_indices[3]].name)

    img = generate_pkm_image(all_pokemon[current_pokemon])
    panel1.configure(image=img)
    panel1.image = img

def next_round(reset_points=False):
    global move_indices, current_pokemon
    if reset_points:
        window.counter = 0
        L['text'] = "Points: 0"

    while True:
        move_indices, current_pokemon = get_new_round()
        move_types = [all_moves[i].type for i in move_indices]
        target_types = all_pokemon[current_pokemon].types
        if is_valid_round(move_types, target_types):
            break

    update_ui()

def handle_action(index):
    move = all_moves[move_indices[index]]
    pokemon = all_pokemon[current_pokemon]

    print(f"Seleccionado: {move.type} vs {pokemon.types}")

    if is_super_effective(move.type, pokemon.types):
        super_effective()
        window.counter += 1
        clicked()
        clicked_max()
        next_round()
    else:
        print("¡Incorrecto!")
        next_round(reset_points=True)

# ==== INTERFAZ TKINTER ====

window = tk.Tk()
window.geometry("1000x820")
window.counter = 0
window.max_counter = 0

def clicked():
    L['text'] = "Points: " + str(window.counter)

def clicked_max():
    if window.counter > window.max_counter:
        window.max_counter = window.counter
        L_max['text'] = "Max. Points: " + str(window.max_counter)

L = Label(window, text="Points: 0", font=("Helvetica", 25), anchor="w", justify="left")
L.pack(side=LEFT, padx=(50, 0))

L_max = Label(window, text="Max. Points: 0", font=("Helvetica", 25), anchor="e", justify="right")
L_max.pack(side=RIGHT, padx=(0, 50))

panel1 = tk.Label(window)
panel1.place(relx=0.5, rely=0.3, anchor=CENTER)

buttonFont = font.Font(family='Helvetica', size=16, weight='bold')

btn1 = tk.Button(window, command=lambda: handle_action(0), height=4, width=25, font=buttonFont)
btn1.place(relx=0.3, rely=0.65, anchor="center")

btn2 = tk.Button(window, command=lambda: handle_action(1), height=4, width=25, font=buttonFont)
btn2.place(relx=0.7, rely=0.65, anchor="center")

btn3 = tk.Button(window, command=lambda: handle_action(2), height=4, width=25, font=buttonFont)
btn3.place(relx=0.3, rely=0.85, anchor="center")

btn4 = tk.Button(window, command=lambda: handle_action(3), height=4, width=25, font=buttonFont)
btn4.place(relx=0.7, rely=0.85, anchor="center")

# ==== INICIAR PRIMERA RONDA ====

move_indices, current_pokemon = get_new_round()
next_round()

window.mainloop()
