#Introdução ao layout em grid
from tkinter import *

menu_principal=Tk()
menu_principal.title("Estudo Tkinter")
# menu_principal.geometry("500x500")



label_1=Label(menu_principal, text="label1", bg="red", font="Arial 20")
label_2=Label(menu_principal, text="label2", bg="green", font="Arial 20")
label_3=Label(menu_principal, text="label3", bg="blue", font="Arial 20")

btn1=Button(menu_principal, text="click1")
btn2=Button(menu_principal, text="click2")
btn3=Button(menu_principal, text="click3")

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=0, column=2)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)


menu_principal.mainloop()