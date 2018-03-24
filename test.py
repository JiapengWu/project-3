from Tkinter import *

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.delete(0, END)
listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

mainloop()