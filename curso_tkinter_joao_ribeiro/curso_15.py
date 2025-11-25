#Continuação do exercicios anterior com widget e eventos
#usando o StringVar

from tkinter import *

#Definir uma função para definir uma ação no commando
def mostrarNome():
    vartexto.set("O teu nome é: " + textobox_1.get())
    
#--------------------------------------------------------
#GUI
root=Tk()
root.title("Titulo da App")
# root.geometry("100x100")

vartexto=StringVar()
#--------------------------------------------------------
#criar os widgets
label_1=Label(root, text="Escreva o teu nome:")
textobox_1=Entry(root)
botao_1=Button(root, text="Executar", command=mostrarNome)
label_2=Label(root, textvariable=vartexto)
label_3=Label(root, textvariable=vartexto)
label_4=Label(root, textvariable=vartexto)

#--------------------------------------------------------
#layout
label_1.grid()
textobox_1.grid()
botao_1.grid()
label_2.grid()
label_3.grid()
label_4.grid()



root.mainloop()