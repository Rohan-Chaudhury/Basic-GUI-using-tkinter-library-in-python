from tkinter import *

root=Tk()

def don():
    print("do nothing")

men = Menu(root)
root.config(menu=men)

subMenu=Menu(men)
men.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New",command=don)
subMenu.add_command(label="old",command=don)
subMenu.add_separator()
subMenu.add_command(label="quit",command=don)

editMenu=Menu(men)
ed=Menu(editMenu)
men.add_cascade(label="edit",menu=editMenu)
editMenu.add_cascade(label="edit",menu=ed)
ed.add_command(label="ed",command=don)

root.mainloop()
