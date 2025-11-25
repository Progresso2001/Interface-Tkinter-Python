"""Label com varias linhas: border, Relief"""
from tkinter import *

menu_principal=Tk()
menu_principal.title("Estudo Tkinter")
menu_principal.geometry("500x300")

label_1=Label(menu_principal, text="flat", 
              font="Arial 20",
              bd=1,
              relief="flat"
              ).pack()

label_2=Label(menu_principal, 
              text="raised", 
              font="Arial 20",
              bd=10,
              relief="raised").pack()

label_3=Label(menu_principal, 
              text="sunken", 
              font="Arial 20",
              bd=10,
              relief="sunken").pack()

label_4=Label(menu_principal, 
              text="solid", 
              font="Arial 20",
              bd=10,
              relief="solid").pack()

label_5=Label(menu_principal, 
              text="ridge", 
              font="Arial 20",
              bd=10,
              relief="ridge").pack()

label_6=Label(menu_principal, 
              text="groove", 
              font="Arial 20",
              bd=10,
              relief="groove").pack()



menu_principal.mainloop()