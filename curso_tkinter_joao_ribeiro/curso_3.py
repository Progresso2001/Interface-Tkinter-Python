"""Alterar a cores e tipo de letras"""

from tkinter import *

menu_principal=Tk()
menu_principal.title("Estudo Tkinter")
menu_principal.geometry("500x300")

#Trabalhando com cores Usando o sistema RGB(Red Green Blue)
#Para melhor informções sobre cores RGB use o site color tutorial
label_1=Label(menu_principal, text= "Este é Label 1",
              bg="#ffaa00",
              fg="red")

label_1.pack()

#Trabalhando com tipo de letras

label_2=Label(menu_principal, text= "Este é Label 2",
              font="Arial 20 bold italic"
              )

label_2.pack()

label_3=Label(menu_principal, text= "Este é Label 3",
              font="verdana 42 bold ",
              fg="#aaaaaa")

label_3.pack()

menu_principal.mainloop()