#TRABALHANDO COM CHECKBUTTON

from tkinter import *

root = Tk()

def apresentar():
    print(valor_check.get())
    
    
valor_check = IntVar()
checar = Checkbutton(
    root,
    text="Está é um checkbox.",
    variable=valor_check,
    command=apresentar
    
    ).pack()

# checar = Checkbutton(
#     root,
#     text="Está é um checkbox."
    
#     ).pack()

root.mainloop()