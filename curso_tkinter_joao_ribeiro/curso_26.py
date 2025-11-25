# TRABALHANDO COM LISTBOX

from tkinter import *

root = Tk()

lista = Listbox(root)
lista.pack()

#inserir um item

# lista.insert(END, "Primeiro item da lista")
# lista .insert(END, "Segundo item da lista")

#Inserir varios itens apartir de uma lista

nomes = ['joaquim', 'joao', 'miguel']
for nome in nomes:
    lista.insert(END, nome)
    
# lista.delete(0,END) #USANDO PARA ELIMINAR OS ELEMENTOS DA LISTA
# lista.delete(1,1)

def executar():
    print(lista.get(ACTIVE))

cmd = Button(root, text="Clique", command=executar).pack()

root.mainloop()