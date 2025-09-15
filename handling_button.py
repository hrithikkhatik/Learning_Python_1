from tkinter import *
window = Tk()
def log_in():
    print("logged in")
button1=Button(command=log_in,text="login",font=("bold",20),bg="red",fg="green",activebackground="black",activeforeground="purple")
button1.pack()
window.mainloop()