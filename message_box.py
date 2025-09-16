from tkinter import *
import tkinter.messagebox

window = Tk()
tkinter.messagebox.showerror("info")
question = tkinter.messagebox.askyesno("today rain or not?")
if question == True:
    print("take a umbrella")
else:
    print("okay")
