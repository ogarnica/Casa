class cuadrado:
    def __init__(self, canvas, tamano, posX, posY):
        self.canvas = canvas
        self.tamano = tamano
        self.posicionx = posX
        self.posiciony = posY

    def paint(self):
        canvas.create_rectangle(self.posicionx, self.posiciony, self.posicionx+self.tamano, self.posiciony+self.tamano)

from tkinter import *
            ##from tkinter.colorchooser import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
oscar   = cuadrado(canvas, 23, 7, 8)
miguel  = cuadrado(canvas, 40, 20, 30)
oscar.paint()
miguel.paint()
