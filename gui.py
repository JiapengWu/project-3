#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  pygui.py
#
'''
Python GUI Tkinter
'''
import os, sys
import tkinter as tk


class Window(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = []

        frame = RadioButtons(container, self)
        frame1 = Option1(container, self)
        frame2 = Option1(container, self)
        self.frames.append(frame)
        self.frames.append(frame1)
        self.frames.append(frame2)
        for f in self.frames:
            f.grid(row=0, column=0, sticky="nsew")
        self.show_frame(0)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class RadioButtons(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Select option:",font=('Arial',10))
        label.pack(pady=10,padx=10)

        option = tk.IntVar()
        option1 = tk.Radiobutton(self,text='1',value=1,variable=option)
        option1.pack(anchor="nw")
        option2 = tk.Radiobutton(self,text='2',value=2,variable=option)
        option2.pack(anchor="nw")

        option1.select()

        select_bt = tk.Button(self,text="Select",command=lambda: controller.show_frame(option.get()))
        quit_bt = tk.Button(self,text="Quit",command=self.quit)
        quit_bt.pack(side='bottom')
        select_bt.pack(side='bottom')


class Option1(tk.Frame):
    '''
        Add a client to the database
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self,text="Do stuff",font=('Arial',10))
        label.pack(pady=10,padx=10)

        stuff = tk.Label(self,text="Stuff")
        stuff.pack()

        self.entryStuff = tk.Entry(self)
        self.entryStuff.pack()

        submit_btn = tk.Button(self,text="Show stuff",command=self.dostuff)
        submit_btn.pack()

        self.showStuff = tk.Label(self,text='')
        self.showStuff.pack()

        goBack = tk.Button(self,text="Back",command=lambda: controller.show_frame(0))
        quit_bt = tk.Button(self,text="Quit",command=self.quit)
        quit_bt.pack(side='bottom')
        goBack.pack(side='bottom')

    def dostuff(self):
        enteredText = self.entryStuff.get()
        self.entryStuff.delete(0, tk.END)
        self.showStuff.config(text=enteredText)


def main(argc, args):
    root = Window()
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()
    root.destroy()
    root.quit()
    return 0


if __name__ == "__main__":
    exit_code = main(len(sys.argv), sys.argv)
    # print("Closing connections")
    # cursor.close()
    # conn.close()
    # server.stop()
    print("Exiting program")
    sys.exit(exit_code)