from tkinter import *


def derecha():
    habitacion.move(1, 10, 0)


def izquierda():
    habitacion.move(1, -10, 0)


def arriba():
    habitacion.move(1, 0, -10)


def abajo():
    habitacion.move(1, 0, 10)

rect_id = []
master = Tk()
habitacion = Canvas(master, width=500, height=500)
habitacion.pack()
for idx in range(10):
    print (idx)
    id=habitacion.create_rectangle(10+10*idx, 10, 20, 20, fill='red')
    rect_id[0] = id
#    print( habitacion.bbox(rect_id[idx]))

mainloop()
