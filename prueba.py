from tkinter import *
import time, random

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
id = canvas.create_rectangle(100, 100, 130, 130, fill='red')


for x in range(500):
    vel_x = 0
    vel_y = 0
    numero = random.randint(1, 4)
    if numero == 1:
        vel_x = 30
    elif numero == 2:
        vel_x = -30
    elif numero == 3:
        vel_y = 30
    elif numero == 4:
        vel_y = -30

    canvas.move(id, vel_x, vel_y)
    pos = canvas.coords(id)
    print(pos)

    if pos[1] <= 0:
        vel_y = 30
    if pos[3] >= 500:
        vel_y = -30
    if pos[0] <= 0:
        vel_x = 30
    if pos[2] >= 500:
        vel_x = -30

    tk.update()
    time.sleep(0.05)