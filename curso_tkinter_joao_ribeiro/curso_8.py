"""Definir e alterar propriedades de um label"""
from tkinter import *

menu_principal=Tk()
menu_principal.title("Estudo Tkinter")
menu_principal.geometry("500x300")

label_1=Label(menu_principal, text="frase de teste", 
              font="Arial 20",
              bd=1,
              relief="solid",
              width=30,
            ).pack()

#outra forma dde definir as propriedades da label

label_2=Label(menu_principal)
label_2['text']="texto da label 2"
label_2['font'] = "Georgia 20"
label_2['bd'] =1
label_2['relief'] = "solid"
label_2.pack()

#Alterar a propriedade da label
label_2['text']="Alterei texto antigo da label "

# print(label_2.keys())#Mostra todos os metodos de uma label

for item in label_2.keys():
    print(item, " : ", label_2[item])

menu_principal.mainloop()