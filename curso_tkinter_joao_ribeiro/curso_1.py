"""Aprender a centralizar o formulario"""
from tkinter import *

menu_principal=Tk()
menu_principal.title("Estudo Tkinter")
menu_principal.geometry("500x300+200+200")

#dimensoes da janela

largura=500
altura=300

# centralizar o formulario
largura_screen=menu_principal.winfo_screenwidth()
altura_screen=menu_principal.winfo_screenheight()

# posicao da janela

posx = largura_screen/2 -largura/2
posy= altura_screen/2 -altura/2

# definir a geometria

menu_principal.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
 
menu_principal.mainloop()