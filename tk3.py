
#Pack tkinter chooses where to place Grid and Place
#Grid you pass placement/details and choose
#Place grid but with more detail
#you can only use 1 type of function for each item out of the 3 in each window
from tkinter import *


root = Tk()

lab1 = Label(root, text="Cool example bro")
b1 = Button(root, text = "Click it NOW")

#Pack method puts everything topcenter by default
#b1.pack()


#TOP LEFT RIGHT BOTTOM
lab1.pack(side = RIGHT)
b1.pack(side = LEFT)



root.mainloop()
