from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Main window")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    label = Label(top, text="This is a Toplevel window")
    label.pack()
    top.mainloop()
l = Label(root, text="This is the main window")
btn = Button(root, text="Open Toplevel window", command=topwin)
l.pack()
btn.pack()
root.mainloop()