"""Definir largura de um label e implicações"""
from tkinter import *

menu_principal=Tk()
menu_principal.title("Estudo Tkinter")
menu_principal.geometry("500x300")

label_1=Label(menu_principal, text="Este é o label 1",
              bg="green",
              font="Arial 10",
              width=20) #usando o metodo width para definir a largura do label
label_1.pack()

label_2=Label(menu_principal, text="Este é o label 2",
              bg="red",
              font="Arial 40",
              width=20)
label_2.pack()

menu_principal.mainloop()