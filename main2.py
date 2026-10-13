from tkinter import *

root = Tk()

root.geometry('600x400')

root.title("Speed Calculator")

def calc_speed():
    distance = int(km_entry.get())
    time = int(h_entry.get())
    speed = distance/time
    end_label.config(text = f"speed: {speed} km/hr")


km_label = Label(root, text = "Enter distance in km :  ", fg = "black", font = ("Arial", 16))

km_label.place(x = 50, y = 50)

km_entry = Entry(root, width = 20)

km_entry.place(x = 300, y = 50)

h_label = Label(root, text = "Enter time in hours :  ", fg = "black", font = ("Arial", 16))

h_label.place(x = 50, y = 100)

h_entry = Entry(root, width = 20)

h_entry.place(x = 300, y = 100)

c_btn = Button(root, text = "Calculate KMPH", bg = "yellow", fg = "black", command = calc_speed)

c_btn.place(x = 200, y = 150)

end_label = Label(root, font = ("Arial", 25), fg = "black")

end_label.place(x = 50, y = 300)

root.mainloop()