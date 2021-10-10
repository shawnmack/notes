import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert("Just a text Widget\nin two lines\n")
T.insert(tk.END, "Jbutt fuck")
tk.mainloop()
