from Tkinter import *
root = Tk()

miFrame = Frame(root, width=400,height =500)

miFondo = PhotoImage(file = "robot.gif")

miFrame.pack()

Label(miFrame, image = miFondo).place(x=50,y=100)

root.mainloop()
