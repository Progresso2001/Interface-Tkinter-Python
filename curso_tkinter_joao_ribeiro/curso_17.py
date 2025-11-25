#Focus e tab order

from tkinter import *

#funcao

def executar():
    l1['text']=t1.get()
    l2['text']=t2.get()
    l3['text']=t3.get()
    
root=Tk()
root.title("App")


#widgets
t1=Entry(root)
t2=Entry(root)
t3=Entry(root)


l1=Label(root)
l2=Label(root)
l3=Label(root)

btn=Button(root, text="Executar", command=executar )

#layout
t3.grid()
t1.grid()
t2.grid()


l1.grid()
l2.grid()
l3.grid()

btn.grid()

#usando o metdo focus
t1.focus()



root.mainloop()

