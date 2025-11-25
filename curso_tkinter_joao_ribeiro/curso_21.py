#SELF, INIT E SUPER

from tkinter import *


#criar classe que vai herdar metodos 

class MinhaFrame(Frame):
    def __init__(self, parent): #o parametro parent indica a quem vamos passar o parametro principal nesse caso o (root)
        #NOTA: pode se usar qualquer letra ou nome no segundo parametro
        #NOTA:Usamos o Self para que a propria classe reconhece o tipo de objecto
        super().__init__()
        self['height'] = 200
        self['width'] = 400
        self['bd'] = 2
        self['bg'] = "green"
        
root = Tk()
root.title("App")

f1 = MinhaFrame(root).pack()



root.mainloop()