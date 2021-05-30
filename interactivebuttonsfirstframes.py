#Functions for buttons - command .config

from tkinter import *

root = Tk()

fr1 = Frame(root)
fr2 = Frame(root)

la1 = Label(fr1,text="Frame One")
butt1= Button(fr1,text='Hit it mr one.')
la2 = Label(fr2,text="Frame Two")
butt2= Button(fr2,text='Hit it twoster.')
la1.pack()
butt1.pack()
la2.pack()
butt2.pack()
fr1.pack(side=LEFT)
fr2.pack(side=RIGHT)
#def button():
#    butt1.config(text="Nice.")



#butt1= Button(root,text='Hit it.',command = button)
#butt1.pack()
root.mainloop()
