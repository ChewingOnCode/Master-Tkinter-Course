# frames are invisible
from tkinter import Frame, Label, Tk

window = Tk()

fTop = Frame(window)
fTop.pack()
fBot = Frame(window)
fBot.pack(side="bottom")

lbl1 = Label(fTop, text="Hello")
lbl2 = Label(fTop, text="Top")
lbl3 = Label(fBot, text="Bottom")

lbl1.pack()
lbl2.pack()
lbl3.pack()

window.mainloop()
