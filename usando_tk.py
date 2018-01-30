from tkinter import *
from tkinter.colorchooser import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_rectangle(10, 10, 50, 50)
c = askcolor()
##c = input('color: ')
canvas.create_text(100, 100, text='hola', font=('Times', 30), fill=c)
