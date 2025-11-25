#Usando HELP para ver propriedades e metodos de uma class

from tkinter import *

class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__
        self['bd'] = 2
        
    

print(help(MinhaFrame))

print(help(Frame))# mostra todos os metodos
