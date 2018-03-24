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

config = "user='cs421g19' host='comp421.cs.mcgill.ca' dbname='cs421' password='Pmdd0301'"
connection = psycopg2.connect(config)
cur = connection.cursor()

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
        frame3 = Option3(container, self)
        frame4 = Option4(container, self)
        frame5 = Option5(container, self)
        frame6 = Option6(container, self)

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
        option1 = tk.Radiobutton(self,text='Option 1: Add a Player to Database',value=1,variable=option)
        option1.pack(anchor="nw")
        option2 = tk.Radiobutton(self,text='Option 2: Get the player with most gold medals in a selected country',value=2,variable=option)
        option2.pack(anchor="nw")
        option3 = tk.Radiobutton(self,text='Option 3: Get the female player with most gold medals for country \n'+
                                            'with most gold medals',value=3,variable=option)
        option3.pack(anchor="nw")
        option4 = tk.Radiobutton(self,text='Option 4: Give medals to each player who won 1st, 2nd or 3rd place \n'+
                                            'in Finals match category',value=4,variable=option)
        option4.pack(anchor="nw")
        option5 = tk.Radiobutton(self,text='Option 5: Update the number of gold/silver/bronze medals for each country, \n'+ 
                                            'given the players that won medals in Finals',value=5,variable=option)
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

        pidentry = tk.Entry(self)
        pidentry.pack()
    
        # name
        text = tk.Label(self,text="What is the player's name?")
        text.pack()

        nameentry = tk.Entry(self)
        nameentry.pack()

        # gender
        text = tk.Label(self,text="What is the player's gender(Male or Female)?")
        text.pack()

        genderentry = tk.Entry(self)
        genderentry.pack()

        #nationality
        text = tk.Label(self,text="What is the player's country")
        text.pack()

        natentry = tk.Entry(self)
        natentry.pack()

        #get the values from user input once all the containers are loaded onto frame
        def getValues():
            pid = pidentry.get()
            name = nameentry.get()
            gender = genderentry.get()
            nationality = natentry.get()
            m.add_single_player(connection, cur, pid, name, gender, nationality, msg)

        #submit
        submit_btn = tk.Button(self,text="SUBMIT",
            command=getValues)
        submit_btn.pack()

        # success message
        msg = tk.StringVar()
        msgLabel = tk.Label(self, textvariable = msg)
        msgLabel.pack()

        goBack = tk.Button(self,text="Back",command=lambda: controller.show_frame(0))
        quit_bt = tk.Button(self,text="Quit",command=self.quit)
        quit_bt.pack(side='bottom')
        goBack.pack(side='bottom')

class Option2(tk.Frame):
    '''
        Get the player who won the most gold medals for a selected country
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self,text="Please enter the country to see the player who won the most gold medals",font=('Arial',10))
        label.pack(pady=10,padx=10)
        label = tk.Label(self,text="Output Format: \"{Player Name}, #medals\" ",font=('Arial',10))
        label.pack(pady=10,padx=10)
        
        # Country
        text = tk.Label(self,text="What is the player's country?")
        text.pack()

        countryentry = tk.Entry(self)
        countryentry.pack()

        # get the values from user input once all the containers are loaded onto frame
        def getValues():
            country = countryentry.get()
            m.player_with_most_gold_medals(connection, cur, country, msg)

        # submit
        submit_btn = tk.Button(self,text="SUBMIT",
            command=getValues)
        submit_btn.pack()

        # success message
        msg = tk.StringVar()
        msgLabel = tk.Label(self, textvariable = msg)
        msgLabel.pack()

        goBack = tk.Button(self,text="Back",command=lambda: controller.show_frame(0))
        quit_bt = tk.Button(self,text="Quit",command=self.quit)
        quit_bt.pack(side='bottom')
        goBack.pack(side='bottom')

class Option3(tk.Frame):
    '''
        Get the female player who won the most gold medals for country with most gold medals
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self,text=
            "Click \"Calculate\" to get the female player who won the most gold medals\n"+
            "for the country with most gold medals",font=('Arial',10))
        label.pack(pady=10,padx=10)

        label = tk.Label(self,text="Output Format: \"{Player Name}, #medals\" ",font=('Arial',10))
        label.pack(pady=10,padx=10)
        
        # get the values from user input once all the containers are loaded onto frame
        def getValues():
            m.female_player_with_most_gold_medals_in_country_with_most_gold_medals(connection, cur, msg)

        # submit
        submit_btn = tk.Button(self,text="CALCULATE",
            command=getValues)
        submit_btn.pack()

        # success message
        msg = tk.StringVar()
        msgLabel = tk.Label(self, textvariable = msg)
        msgLabel.pack()

        goBack = tk.Button(self,text="Back",command=lambda: controller.show_frame(0))
        quit_bt = tk.Button(self,text="Quit",command=self.quit)
        quit_bt.pack(side='bottom')
        goBack.pack(side='bottom')


class Option4(tk.Frame):
    '''
        Give medals to each player who won 1st, 2nd or 3rd place in Finals match category
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self,text=
            "Click \"Update\" give medals to each player who won 1st, 2nd or 3rd place in Finals match category",font=('Arial',10))
        label.pack(pady=10,padx=10)
        
        # get the values from user input once all the containers are loaded onto frame
        def getValues():
            m.update_player_medal(connection, cur, msg)

        # submit
        submit_btn = tk.Button(self,text="Update",
            command=getValues)
        submit_btn.pack()

        # success message
        msg = tk.StringVar()
        msgLabel = tk.Label(self, textvariable = msg)
        msgLabel.pack()

        goBack = tk.Button(self,text="Back",command=lambda: controller.show_frame(0))
        quit_bt = tk.Button(self,text="Quit",command=self.quit)
        quit_bt.pack(side='bottom')
        goBack.pack(side='bottom')

class Option5(tk.Frame):
    '''
        Update the number of gold, silver, bronze medals for each country given the players that won medals in Finals
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self,text=
            "Click \"Update\" update the number of gold, silver, bronze medals for each country,\n"+ 
            "given the players that won medals in Finals",font=('Arial',10))
        label.pack(pady=10,padx=10)
        
        # get the values from user input once all the containers are loaded onto frame
        def getValues():
            m.update_country_medal(connection, cur, msg)

        # submit
        submit_btn = tk.Button(self,text="Update",
            command=getValues)
        submit_btn.pack()

        # success message
        msg = tk.StringVar()
        msgLabel = tk.Label(self, textvariable = msg)
        msgLabel.pack()

        goBack = tk.Button(self,text="Back",command=lambda: controller.show_frame(0))
        quit_bt = tk.Button(self,text="Quit",command=self.quit)
        quit_bt.pack(side='bottom')
        goBack.pack(side='bottom')

class Option6(tk.Frame):
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
        # pid = entryStuff.get()
        self.entryStuff.delete(0, tk.END)
        self.showStuff.config(text=enteredText)




def main():
    root = Window()
    root.title("Olympics Database Project GUI")
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()
    root.destroy()
    root.quit()
    return 0


if __name__ == "__main__":
    exit_code = main()
    print("Closing connections")
    cur.close()
    connection.close()
    # server.stop()
    print("Exiting program")
    sys.exit(exit_code)
