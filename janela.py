from tkinter import *

janela=Tk()
janela.title("Minha janela em Tkinter.")
janela.configure(background='white')
janela.geometry("250x250")

# label_1=Label(janela,  width=10, height=2, text='Nome', font=('Arial 10'))
# label_1.place(x=10, y=10)



# label_2=Label(janela,  width=10, height=2, text='idade', font=('Arial 10 bold'))
# label_2.place(x=10, y=60)



# label_3=Label(janela,  width=10, height=2,  text='cidade', font=('Arial 10 '))
# label_3.place(x=20, y=110)

# rota=Label(janela, text='ola')
# rota.pack(side='right')

rota=Label(janela, text='Nome')
rota.grid(row=0, column=0)

rota_1=Label(janela, text='idade')
rota_1.grid(row=0, column=1)

rota_2=Label(janela, text='cidade')
rota_2.grid(row=1, column=1)

rota_1=Label(janela, text='pais')
rota_1.grid(row=4, column=2)

  




janela.mainloop()