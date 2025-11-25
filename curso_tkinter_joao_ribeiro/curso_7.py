"""Padding e Justifição de texto """

from tkinter import *

menu_principal=Tk()
menu_principal.title("Estudo Tkinter")
menu_principal.geometry("500x300")

label_1=Label(menu_principal, text="frase de testes\nBom teste", 
              font="Arial 20",
              bd=1,
              relief="solid",
              width=30,
              height=5,
              justify=CENTER,
              anchor=W
              ).pack()

label_2=Label(menu_principal, text="frase de testes\noutra frase de testes\ntestes", 
              font="Arial 20",
              bd=1,
              relief="solid",
              padx=10,
              pady=10,
              justify=RIGHT
              ).pack()

menu_principal.mainloop()