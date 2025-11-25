import tkinter as tk

# Criar a janela principal
root = tk.Tk()
root.title("Login Simples")
root.geometry("300x220")

# Frame central para alinhar os widgets
frame_central = tk.Frame(root)
frame_central.pack(expand=True)

# Título centralizado no topo
titulo = tk.Label(frame_central, text="Página de Login", font=("Arial", 16))
titulo.grid(row=0, column=0, columnspan=2, pady=(10, 10))

# Campo Nome
tk.Label(frame_central, text="Nome:").grid(row=1, column=0, sticky="e", pady=5)
entrada_nome = tk.Entry(frame_central)
entrada_nome.grid(row=1, column=1, pady=5)

# Campo Senha
tk.Label(frame_central, text="Senha:").grid(row=2, column=0, sticky="e", pady=5)
entrada_senha = tk.Entry(frame_central, show="*")
entrada_senha.grid(row=2, column=1, pady=5)

# Frame para os botões de rádio
frame_radios = tk.Frame(frame_central)
frame_radios.grid(row=3, column=0, columnspan=2, pady=5)

var_radio = tk.StringVar(value="")

# Rádio botão Lembrar à esquerda
radio_lembrar = tk.Radiobutton(frame_radios, text="Lembrar", variable=var_radio, value="lembrar")
radio_lembrar.pack(side="left", padx=10)

# Rádio botão Esquecer à direita
radio_esquecer = tk.Radiobutton(frame_radios, text="Esquecer", variable=var_radio, value="esquecer")
radio_esquecer.pack(side="right", padx=10)

# Botão Enviar centralizado
botao_enviar = tk.Button(frame_central, text="Enviar")
botao_enviar.grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Centralizar a janela na tela
root.eval('tk::PlaceWindow . center')

root.mainloop()
