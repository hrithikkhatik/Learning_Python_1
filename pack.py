from tkinter import *
window = Tk()
label1= Label(text="label-1",bg="red",fg="white")
label2 = Label(text="label-2",bg="yellow",fg="black")
label3= Label(text="label-3",bg="green",fg="yellow")
label1.pack(side="top",fill="x",expand=False)
label2.pack(side="left",fill="y",expand=False)
label3.pack(side="bottom",fill="y",expand=False)
window.mainloop()