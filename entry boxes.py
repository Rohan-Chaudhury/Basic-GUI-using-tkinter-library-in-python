from tkinter import *

root= Tk()

l1=Label(root,text="Name")
l2=Label(root,text="Password")
e1=Entry(root)
e2=Entry(root)

l1.grid(sticky=E)#grid takes N,S,E,W,N for north
l2.grid(row=1,column=0,sticky=E)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

c=Checkbutton(root,text="keep me logged in")
c.grid(columnspan=2)


root.mainloop()
