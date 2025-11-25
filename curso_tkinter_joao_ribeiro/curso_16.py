#Conversao de unidades FAHRENHEIT PARA CELSIUS

from tkinter import *


#DEefinir a função calcular 
#formula: C = (F-32) * 5/6
def calcular():
    F = float(textbox_1.get())
    C = (F-32) * 5/6
    final.set(str(round(C,1)) + " graus celsius")
root=Tk()
root.title("Conversao")

final=StringVar()


#widgets

label_1=Label(root, text="Grau Fahrenheit:")
textbox_1=Entry(root)
botao_1=Button(root, text="Calcular", command=calcular)
label_resultado=Label(root, textvariable=final)

#layout
label_1.grid()
textbox_1.grid()
botao_1.grid()
label_resultado.grid()

root.mainloop()

