from tkinter import *

root = Tk()
def nameSub():
    print("Your name is: {}".format(e1.get()))
    la1.config(text=e1.get())
e1 = Entry(root)
la1= Label(root,text="What's your name?")
butt1= Button(root,text="Submit",command=nameSub)


la1.pack()
butt1.pack()
e1.pack()
