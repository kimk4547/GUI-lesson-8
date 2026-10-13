from tkinter import *

from time import strftime

root = Tk()

root.title("Digital Clock")

time_label = Label(root, fg = "black", bg = "turquoise", font = ("calibri", 40, "bold"))

time_label.pack(anchor = "center")

def time():
    string = strftime("%H:%M:%S %p")
    time_label.config(text = string)
    time_label.after(1000, time)

time()

root.mainloop()