#Adicionar Imagem a um Layout

from tkinter import  * 

root = Tk()

img=PhotoImage(file="curso_tkinter_joao_ribeiro/curso_24_images/logotipo.png")

label_imagem = Label(root, image=img).pack()

root.mainloop()