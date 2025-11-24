import tkinter as tk

janela=tk.Tk()
janela.title("Login Pagina")
janela.geometry("400x350")

#Frame para centralizar o widget

frame_central=tk.Frame(janela)
frame_central.pack(expand=True)

#centralizar o Titulo no top

titulo=tk.Label(frame_central, text="Página de Cadastro de aluno", font=("Arial 16 bold"))
titulo.grid(row=0, column=0, columnspan=2, pady=(10, 10))

#Criar campo Nome

tk.Label(frame_central, text="Nome do aluno:", font=("Arial 10 bold")).grid(row=1, column=0, sticky="e", pady=5)
inserir_nome=tk.Entry(frame_central)
inserir_nome.grid(row=1, column=1, pady=5)

#Campo de Senha
tk.Label(frame_central, text="Inserir a senha:", font=("Arial 10 bold")).grid(row=2, column=0, sticky="e", pady=5)
inserir_senha=tk.Entry(frame_central, show="*")
inserir_senha.grid(row=2, column=1, pady=5)


#frame para botoes de radio 

frame_radio=tk.Frame(frame_central)
frame_radio.grid(row=3, column=0, columnspan=2, pady=5)
var_radio=tk.StringVar()

# Rádio botão Lembrar à esquerda
radio_lembrar = tk.Radiobutton(frame_radio, text="Lembrar", variable=var_radio, value="lembrar")
radio_lembrar.pack(side="left", padx=10)

# Rádio botão esquecer à direta
radio_lembrar = tk.Radiobutton(frame_radio, text="Esquecer", variable=var_radio, value="esquecer")
radio_lembrar.pack(side="right", padx=10)

#Botão Enviar centralizad

botao_enviar=tk.Button(frame_central, text="Enviar", font=("Arial 10 bold"))
botao_enviar.grid(row=4, column=0, columnspan=2, pady=(20, 10))

#centralizar a janela da tela

janela.eval("tk::PlaceWindow . left")

janela.mainloop()