#Trabalhando com MESSAGE

from tkinter import *

root  = Tk()
root.geometry("400x300")

minha_mensagem  = Message(root, text="Este é o texto do message widget.", width= 100 )
minha_mensagem.pack()

root.mainloop()