"""Altura de uma label"""

from tkinter import *

menu_principal=Tk()
menu_principal.title("Estudo Tkinter")
menu_principal.geometry("500x300")

label_1=Label(menu_principal, text="0123456789", 
              font="Arial 20",
              bd=1,
              relief="solid",
              width=25,
              height=4, #height para determinar a altura da label
              anchor=CENTER
              ).pack()




menu_principal.mainloop()