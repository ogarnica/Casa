from tkinter import *
#from star import star

tk = Tk()
#boton = Button(tk , text="hola")
boton = Button(tk , text="hola", command = print("Apretar boton"))
boton.pack( )
tk.mainloop()