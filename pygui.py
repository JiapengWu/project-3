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
import modules as m
import psycopg2


class Window(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = []
        #create 'pages' for each option
        frame = RadioButtons(container, self) #main menu
        frame1 = Option1(container, self)
        frame2 = Option2(container, self)
        frame3 = Option1(container, self)
        frame4 = Option1(container, self)
        frame5 = Option1(container, self)
        frame6 = Option1(container, self)

        #append each 'page' to a list
        self.frames.append(frame)
        self.frames.append(frame1)
        self.frames.append(frame2)
        self.frames.append(frame3)
        self.frames.append(frame4)
        self.frames.append(frame5)
        self.frames.append(frame6)

        #go through list to find the right page to load based on option selected
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

        #Option menu
        option = tk.IntVar()
        option1 = tk.Radiobutton(self,text='Option 1 : Add a Player to Database',value=1,variable=option)
        option1.pack(anchor="nw")
        option2 = tk.Radiobutton(self,text='Option 2',value=2,variable=option)
        option2.pack(anchor="nw")
        option3 = tk.Radiobutton(self,text='Option 3',value=3,variable=option)
        option3.pack(anchor="nw")
        option4 = tk.Radiobutton(self,text='Option 4',value=4,variable=option)
        option4.pack(anchor="nw")
        option5 = tk.Radiobutton(self,text='Option 5',value=5,variable=option)
        option5.pack(anchor="nw")
        option6 = tk.Radiobutton(self,text='Option 6',value=6,variable=option)
        option6.pack(anchor="nw")

        option1.select() #default select option 1

        select_bt = tk.Button(self,text="Select",command=lambda: controller.show_frame(option.get()))
        quit_bt = tk.Button(self,text="Quit",command=self.quit)
        quit_bt.pack(side='bottom')
        select_bt.pack(side='bottom')


class Option1(tk.Frame):
    '''
        Add a player to the database
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self,text="Please fill the player information",font=('Arial',10))
        label.pack(pady=10,padx=10)
        #pid
        text = tk.Label(self,text="What is the player's pid? It has to be greater than 0")
        text.pack()

        entryStuff = tk.Entry(self)
        entryStuff.pack()
        pid = entryStuff.get()
        entryStuff.delete(0, tk.END)
    
        # # name
        # text = tk.Label(self,text="What is the player's name?")
        # text.pack()

        # self.entryStuff = tk.Entry(self)
        # self.entryStuff.pack()
        # name = self.entryStuff.get()
        # # gender
        # text = tk.Label(self,text="What is the player's gender(Male or Female)?")
        # text.pack()

        # self.entryStuff = tk.Entry(self)
        # self.entryStuff.pack()
        # gender = self.entryStuff.get()

        # #nationality
        # text = tk.Label(self,text="What is the player's country")
        # text.pack()

        self.entryStuff = tk.Entry(self)
        self.entryStuff.pack()
        nationality = self.entryStuff.get()

        #submit
        submit_btn = tk.Button(self,text="SUBMIT",
            # command=lambda: m.add_single_player(cur, pid, name, gender, nationality))
            command=lambda: m.add_single_player(cur, pid, None, None, None))
        submit_btn.pack()

        goBack = tk.Button(self,text="Back",command=lambda: controller.show_frame(0))
        quit_bt = tk.Button(self,text="Quit",command=self.quit)
        quit_bt.pack(side='bottom')
        goBack.pack(side='bottom')

class Option2(tk.Frame):
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


def main(cur):
    root = Window()
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()
    root.destroy()
    root.quit()
    return 0


if __name__ == "__main__":
    config = "user='cs421g19' host='comp421.cs.mcgill.ca' dbname='cs421' password='Pmdd0301'"
    connection = psycopg2.connect(config)
    cur = connection.cursor()
    exit_code = main(cur)
    print("Closing connections")
    cur.close()
    connection.close()
    # server.stop()
    print("Exiting program")
    sys.exit(exit_code)