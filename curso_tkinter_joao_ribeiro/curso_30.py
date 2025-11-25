#Adicionar Menus a aplicação

from tkinter import * 

root = Tk()
root.geometry("300x200")


meu_menu = Menu(root)


filemenu= Menu(meu_menu, tearoff=0)
#Menu file
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
meu_menu.add_cascade(label="file", menu=filemenu)

#Menu Edit
fileEdit= Menu(meu_menu, tearoff=0)
fileEdit.add_command(label="Copy")
fileEdit.add_command(label="Paste")
fileEdit.add_command(label="Select All")
meu_menu.add_cascade(label="Edit", menu=fileEdit)

root.config(menu=meu_menu)

root.mainloop()