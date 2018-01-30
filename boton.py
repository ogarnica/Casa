from tkinter import *
def click():
    print('click')

tk = Tk()
btn = Button(tk, text='cick me', command=click)
btn.pack()
