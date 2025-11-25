#Pequenos exercicios com widget e eventos

# from tkinter import *

# #Definir uma função para definir uma ação no commando
# def mostrarNome():
#     nome=textobox_1.get()
#     label_final=Label(root, text="O teu nome é: " + nome)
#     label_final.grid()

# #GUI
# root=Tk()
# root.title("Titulo da App")
# root.geometry("200x100")

# #criar os widgets
# label_1=Label(root, text="Escreva o teu nome:")
# textobox_1=Entry(root)
# botao_1=Button(root, text="Executar", command=mostrarNome)

# #organizar os widgets

# label_1.grid()
# textobox_1.grid()
# botao_1.grid()

# root.mainloop()

from tkinter import *

def comentar():
    comentario=textobox.get()
    ult_label=Label(janela, text="Seu comentario: " + comentario)
    ult_label.grid()
    
janela=Tk()
janela.title("Comentários")
janela.geometry("300x200")

label=Label(janela, text="Comenta qualquer coisa aqui: ")
textobox=Entry(janela)
botao=Button(janela, text='Enviar', command=comentar)

label.grid()
textobox.grid()
botao.grid()

janela.mainloop()