from tkinter import Button, Tk

window = Tk()


def handleClick():
    print("Handle was Clicked")


btn = Button(
    window,
    border=2,
    background="Green",
    foreground="White",
    text="Click Me",
    padx=50,
    pady=80,
    command=handleClick,
)
btn.place(x=50, y=50)

window.mainloop()
