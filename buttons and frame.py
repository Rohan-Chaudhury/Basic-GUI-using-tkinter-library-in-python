from tkinter import *

root= Tk()
topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

button1= Button(topframe, text="button 1",fg="red")
button2= Button(topframe, text="button 2",fg="blue")
button3= Button(topframe, text="button 3",fg="yellow")
button4= Button(bottomframe, text="button 4",fg="orange")


button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack()
button4.pack(side=BOTTOM)


root.mainloop()
