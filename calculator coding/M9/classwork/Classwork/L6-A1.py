from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title('Denomination Counter')
root.configure(bg='lightblue')
root.geometry('650x400')

upload = Image.open('img.jpg')
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='blue')
label.place(x=180, y=20)

label1 = Label(root,
               text = 'Denomination Counter',
               bg='lightblue',)
label1.place(x=180, y=340)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination?"
    )
    if MsgBox == 'ok':
        topwin()
        
button1 = Button(
    root,
    text = "let's get started",
    command = msg,
    bg='lightgreen',
    fg='black'
)
button1.place(x=250, y=350)
def topwin():
    top = Toplevel()
    top.geometry("400x400")
    top.title("Denomination Calculator")
    top.configure(bg='lightyellow')

    label1 = Label(top, text="Enter the amount", bg='lightyellow')
    entry = Entry(top)
    lb = Label(top, text="Some are number of notes for each denomination", bg='lightyellow')
    
    lb1 = Label(top, text="2000 ", bg='lightyellow')
    lb2 = Label(top, text="500 ", bg='lightyellow')
    lb3 = Label(top, text="100 ", bg='lightyellow')
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator():
        try:
            global amount
            amount = int(entry.get())
            n2000 = amount // 2000
            amount %= 2000
            n500 = amount // 500
            amount %= 500
            n100 = amount // 100
            amount %= 100
            
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(END, str(n2000))
            t2.insert(END, str(n500))
            t3.insert(END, str(n100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a solid number.")
            
    btn = Button(top, text="Calculate", command=calculator, bg='lightgreen')
    label1.pack(x=200, y=20)
    entry.place(x=200, y=40)
    btn.place(x=200, y=80)
    lb1.place(x=100, y=150)
    t1.place(x=200, y=150)
    lb2.place(x=100, y=200)
    t2.place(x=200, y=200)
    lb3.place(x=100, y=250)
    t3.place(x=200, y=250)
    top.mainloop()
root.mainloop()