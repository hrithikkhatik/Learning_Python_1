from tkinter import *
window = Tk()
c = Canvas(window,width=500,height=700)
c.pack()
c.create_line((0,0,500,500),fill="red")
c.create_line((0,500,500,0),fill="red")
c.create_rectangle(200,200,400,400,fill="orange",outline="green")
window.mainloop()
