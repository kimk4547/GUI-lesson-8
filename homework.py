from tkinter import *

from time import strftime

import random

root = Tk()

root.title("Party Clock")

time_label = Label(root, fg = "black", bg = "turquoise", font = ("calibri", 40, "bold"))

time_label.pack(anchor = "center")

color_list = ['red', 'blue', 'green', 'purple', 'orange', 'pink']

def time():
    string = strftime("%H:%M:%S %p")
    random.choice(color_list)
    time_label.config(text = string, fg = random.choice(color_list))
    time_label.after(1000, time)
 

time()

root.mainloop()