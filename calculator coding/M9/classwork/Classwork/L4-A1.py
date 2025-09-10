from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.geometry("500x500")

greeting = Label(text="Hello User!", fg='black',bg='white')
button = Button(text="Click Me!", fg='black',bg='white')
entry = Entry(fg="yellow",bg="blue",width=100)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window,relief=RAISED,borderwidth=5)
frame.pack()
label = Label(master=frame,text="This is a frame")
label.pack()

textbox = Text(fg='green',bg='white')

textbox.pack()
window.mainloop()