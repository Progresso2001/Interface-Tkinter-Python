#Trabalhando RADIOBUTTON

from tkinter import *

root  = Tk()
root.geometry("400x300")

valor_a =  IntVar()



radio_1=Radiobutton(root, text="Opção 1", variable=valor_a, value=1 )
radio_2=Radiobutton(root, text="Opção 2", variable=valor_a, value=2)
radio_3=Radiobutton(root, text="Opção 3", variable=valor_a, value=3)
radio_1.pack()
radio_2.pack()
radio_3.pack()

# radio_1.select()

#definir funcao
def ver_radio():
    print(valor_a.get())

cmd = Button(root, text="Executar", command=ver_radio)
cmd.pack()

root.mainloop()