from tkinter import *

def derecha(event):
    canvas.move(1, 10, 0)

def izquierda(event):
    canvas.move(1, -10, 0)

def arriba(event):
    canvas.move(1, 0, -10)

def abajo(event):
    canvas.move(1, 0, 10)

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.bind_all('<KeyPress-Right>', derecha)
canvas.bind_all('<KeyPress-Left>', izquierda)
canvas.bind_all('<KeyPress-Up>', arriba)
canvas.bind_all('<KeyPress-Down>', abajo)
