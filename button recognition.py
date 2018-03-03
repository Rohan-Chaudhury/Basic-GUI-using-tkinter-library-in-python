from tkinter import *

root= Tk()

def leftc(a):
    print("left")
def middlec(a):
    print("middle")
def rightc(a):
    print("right")

frame=Frame(root,width=300,height=250)
frame.bind("<Button-1>",leftc)
frame.bind("<Button-2>",middlec)
frame.bind("<Button-3>",rightc)
frame.pack()


root.mainloop()
