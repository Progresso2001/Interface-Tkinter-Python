#Label TEXTVARIABLE E STRINGVAR
from tkinter import *

menu_principal=Tk()
menu_principal.title("Estudo Tkinter")
menu_principal.geometry("500x300")


texto=StringVar()

texto.set("Novo texto criado")

label_1=Label(menu_principal,
              font="Arial 20",
              bg="red",
              fg="white",
              textvariable=texto
              )
texto.set("Jaoaqui Eliseu")#Alteração do texto

label_1.pack()

label_2=Label(menu_principal,
              font="Arial 20",
              bg="#f1f10e",
              fg="white",
              textvariable=texto
              )

label_2.pack()

label_3=Label(menu_principal,
              font="Arial 20",
              bg="blue",
              fg="white",
              textvariable=texto
              )

label_3.pack()

label_4=Label(menu_principal,
              font="Arial 20",
              bg="#bbbb0b",
              fg="white",
              textvariable=texto
              )

label_4.pack()


menu_principal.mainloop()