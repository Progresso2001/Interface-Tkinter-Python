#Columnspan em GRID
from tkinter import *

root=Tk()
root.title("Login")

# Label(root, width=20, bg="red").grid(column=0)
# Label(root, width=20, text="texto criado", bg="green").grid(column=1)

# # Label(root, width=40, text="texto criado", bg="blue").grid(column=0)#com espaço sobrando

# Label(root, text="texto criado", bg="blue").grid(columnspan=2, sticky="we")#com espaço preenchido


#usando columnspan

Label(root, bg="red").grid(column=0)
Label(root, text="texto criado", bg="green").grid(column=1)
Label(root, text="texto criado", bg="red").grid(column=2)
Label(root, text="texto criado", bg="blue").grid(columnspan=3, sticky="we")





root.mainloop()

"""parâmetro columnspan serve para fazer com que um widget ocupe mais de uma coluna na grade (grid) onde ele está disposto. Por padrão, 
cada widget ocupa uma única célula da grade, ou seja, uma coluna e uma linha. Ao usar columnspan, você especifica quantas colunas consecutivas o widget deve abranger, 
fazendo com que ele "estique" horizontalmente por essas colunas.

Por exemplo, se você definir columnspan=2 para um widget colocado na coluna 0, 
ele irá ocupar as colunas 0 e 1 da grade, 
como se estivesse fundindo essas duas células horizontais em uma só para aquele widget.


"""