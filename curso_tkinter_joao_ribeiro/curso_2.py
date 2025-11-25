"""Label widget"""

from tkinter import *

menu_principal=Tk()
menu_principal.title("Estudo Tkinter")

label_1=Label(menu_principal, text="Este é label 1.")
# label_1.pack()

label_2=Label(menu_principal, text="Este é label 2.")
# label_2.pack()

cmd=Button(menu_principal, text="Executar")
# cmd.pack()

#pack
cmd.pack()
label_2.pack()
label_1.pack()



menu_principal.mainloop()