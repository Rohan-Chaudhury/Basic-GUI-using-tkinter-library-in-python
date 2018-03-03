from tkinter import *

class Buttons:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.printbutton = Button(frame,text="print",command=self.printMessage)
        self.printbutton.pack(side=LEFT)

        self.quitButton = Button(frame,text="quit",command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("wow this actually worked")
        



root= Tk()

b=Buttons(root)
root.mainloop()
