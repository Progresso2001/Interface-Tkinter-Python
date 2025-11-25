# EXERCICIOS PRATICOS COM FRAMES DE INSTANCIAÇÃO

from tkinter import *

class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self['bd'] = 1
        self['relief']  ="solid"
        
        self.text_1_text = StringVar()
        self.label_1_text = StringVar()
        
        #widgets
        self.label_1 = Label(self, textvariable=self.label_1_text).grid()
        text_1  = Entry(self, textvariable=self.text_1_text).grid()
        
        #botao
        cmd_1 = Button(self, text="Clique", command=self.executar).grid()
        
    def executar(self):
        self.label_1_text.set("Óla, " + self.text_1_text.get() + ".")
            
root = Tk()
root.title("App")
root.geometry("200x200")
frame_1 = MinhaFrame(root).grid()

 
root.mainloop()