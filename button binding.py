from tkinter import *

root= Tk()

def printn(a):
    print("sjdajksdhajsd")

button1=Button(root,text="print my name")
button1.bind("<Button-3>",printn)#right mouse click
button1.pack()


root.mainloop()
