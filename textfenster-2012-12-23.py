#!/usr/bin/python3


from tkinter import *
root = Tk()
textfenster = Text(root)
textfenster.pack()

def hole():
        print (textfenster.get('1.0',END))
        
but = Button(root,text='Hole', command = hole)
but.pack(side = LEFT)
root.mainloop()

