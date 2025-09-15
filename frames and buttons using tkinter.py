# frame using tkinter
"""
from tkinter import *
window = Tk()
inp = Label(window,text="hello world")
inp.pack()
window.title("hrithik")
window.config(bg="white")
window.geometry("700x300")
frame1 = Frame(window,bg="orange",height=300,width=2000,cursor="dot")
frame2 = Frame(window,bg="green",height=300,width=2000,cursor="dotbox")
frame1.pack(side="top")
frame2.pack(side="bottom")
window.mainloop()
"""
# button using tkinter
from tkinter import *
window = Tk()
inp = Label(window,text="hello world")
inp.pack()
window.title("HRITHIK")
window.geometry("700x300")
window.config(bg="yellow")
frame1 = Frame(window,width=200,height=100,cursor="dot")
frame2 = Frame(window,width=200,height=100,cursor="dotbox")
frame1.pack(side="top")
frame2.pack(side="bottom")
button1= Button(frame1,bg="white",text="button1")
button2 = Button(frame2,bg="white",text="button2")
button3 = Button(frame1,fg="black",text="button3")
button1.pack(side="top")
button2.pack(side="bottom")
button3.pack(side="top")
window.mainloop()



