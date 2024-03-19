# Windows and Labels
import tkinter

window = tkinter.Tk()

# pack() -widget similar to .grid() to "pack" all the widgets one after another
# in a window.
lblHello = tkinter.label(window, text="Hello World")
lblHello.pack()

window.mainloop()

# Frames
