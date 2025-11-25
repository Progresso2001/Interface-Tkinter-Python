#CRIar executavel  com pyinstaller

from tkinter import *

root = Tk()
root.geometry("300x200")

texto = StringVar()

texto.set("")

label_1 = Label(root, textvariable=texto)
label_1.pack()

def executar():
    texto.set("Texto alterado")
    
cmd =Button(root, text="Executar", command=executar)

cmd.pack()

    
root.mainloop()