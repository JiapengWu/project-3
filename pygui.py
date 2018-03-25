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
import re

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
        main_frame = RadioButtons(container, self) #main menu
        frame_1 = Option1(container, self)
        frame_2 = Option2(container, self)
        frame_3 = Option3(container, self)
        frame_4 = Option4(container, self)
        frame_5 = Option5(container, self)
        frame_6 = Option6(container, self)
        frame_7 = Option7(container, self)

        #append each 'page' to a list
        self.frames.append(main_frame)
        self.frames.append(frame_1)
        self.frames.append(frame_2)
        self.frames.append(frame_3)
        self.frames.append(frame_4)
        self.frames.append(frame_5)
        self.frames.append(frame_6)
        self.frames.append(frame_7)
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
        option3 = tk.Radiobutton(self,text='Option 3: Get the female player with most gold medals in country winning the most gold medals'
                                                                ,value=3,variable=option)
        option3.pack(anchor="nw")
        option4 = tk.Radiobutton(self,text='Option 4: Update the number of gold, silver and bronze medals for each player'
                                                                ,value=4,variable=option)
        option4.pack(anchor="nw")
        option5 = tk.Radiobutton(self,text='Option 5: Update the number of gold, silver and bronze medals for each country'
                                                                ,value=5,variable=option)
        option5.pack(anchor="nw")
        option6 = tk.Radiobutton(self,text='Option 6: Find all players who got gold medals in a given \'category\' in a match'
                                                                ,value=6,variable=option)
        option6.pack(anchor="nw")

        option7 = tk.Radiobutton(self,text='Option 7: Add a new participation record',value=7,variable=option)
        option7.pack(anchor="nw")


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
        text = tk.Label(self,text="What is the player's gender (Male or Female)?")
        text.pack()

        genderentry = tk.Entry(self)
        genderentry.pack()

        # nationality
        text = tk.Label(self,text="What is the player's country? Select from the list below:")
        text.pack()


        try:
            cur.execute('select cname from country')
            result = cur.fetchall()
            connection.commit()
            countries = list(map(lambda x:x[0], result))
        except psycopg2.Error as e:
            connection.rollback()

        def get_nationality():
            nationality['text'] = "You selected: " + mylist.get("active")

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        mylist = tk.Listbox(self, yscrollcommand=scrollbar.set)
        for i in range(len(countries)):
            mylist.insert(tk.END, countries[i])

        mylist.pack()
        scrollbar.config(command=mylist.yview)

        select_btn = tk.Button(self,text="Select",
            command=get_nationality)
        select_btn.pack()

        nationality = tk.Label(self, text="")
        nationality.pack()

        #get the values from user input once all the containers are loaded onto frame
        def getValues():
            pid = pidentry.get()
            name = nameentry.get()
            gender = genderentry.get()
            nat = nationality["text"].split(":")[-1].strip()
            pidentry.delete(0, tk.END)
            genderentry.delete(0, tk.END)
            nameentry.delete(0, tk.END)
            m.add_single_player(connection, cur, pid, name, gender, nat, msg)

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
        
        # Country
        text = tk.Label(self,text="What is the player's country?")
        text.pack()

        try:
            cur.execute('select cname from country')
            result = cur.fetchall()
            connection.commit()
            countries = list(map(lambda x:x[0], result))
        except psycopg2.Error as e:
            connection.rollback()

        def get_nationality():
            nationality['text'] = "You selected: " + mylist.get("active")

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        mylist = tk.Listbox(self, yscrollcommand=scrollbar.set)
        for i in range(len(countries)):
            mylist.insert(tk.END, countries[i])

        mylist.pack()
        scrollbar.config(command=mylist.yview)

        select_btn = tk.Button(self,text="Select",
            command=get_nationality)
        select_btn.pack()

        # get the values from user input once all the containers are loaded onto frame
        def getValues():
            nat = nationality["text"].split(":")[-1].strip()
            m.player_with_most_gold_medals(connection, cur, nat, msg)

        nationality = tk.Label(self, text="")
        nationality.pack()

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

        # label = tk.Label(self,text="Output Format: \"{Player Name}, #medals\" ",font=('Arial',10))
        # label.pack(pady=10,padx=10)
        
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
    '''
        Find all players who got gold and participated in a specific category of a match
    '''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # code for scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        label = tk.Label(self, text="", font=('Arial', 10))
        label.pack(pady=10, padx=10)

        # stype
        text = tk.Label(self, text="Please select the stype:")
        text.pack()

        stype_list = tk.Listbox(self)
        stype_list.insert(tk.END, "Swimming")
        stype_list.insert(tk.END, "Athletics")
        # for i in range(len(countries)):
        #     stype_list.insert(tk.END, countries[i])

        stype_list.pack()

        def get_stype():
            stype = stype_list.get("active")
            stype_label['text'] = "You selected: " + stype
            try:
                cur.execute('select team_type from sports where stype = %s', (stype,))
                team_types = set(map(lambda x: x[0], cur.fetchall()))
                for team_type in team_types:
                    team_type_list.insert(tk.END, team_type)
                connection.commit()
            except psycopg2.Error as e:
                connection.rollback()
                # msg_1.set(e.pgerror)

        # next
        select_btn = tk.Button(self,text="Select",
            command=get_stype)
        select_btn.pack()

        stype_label = tk.Label(self, text="")
        stype_label.pack()


        # team_type
        text = tk.Label(self, text="Please select the team type:")
        text.pack()

        team_type_list = tk.Listbox(self)
        team_type_list.pack()

        def get_team_type():

            stype = stype_label["text"].split(":")[-1].strip()
            team_type = team_type_list.get("active")
            team_type_label['text'] = "You selected: " + team_type

            try:
                cur.execute("select gender from sports where stype = %s and team_type = %s", (stype, team_type,))
                genders = set(map(lambda x: x[0], cur.fetchall()))
                for gender in genders:
                    gender_list.insert(tk.END, gender)
                connection.commit()
            except psycopg2.Error as e:
                connection.rollback()
                # controller.show_frame(6)

        select_btn = tk.Button(self,text="Select",
            command=get_team_type)
        select_btn.pack()

        team_type_label = tk.Label(self, text="")
        team_type_label.pack()



        # gender
        text = tk.Label(self, text="What is the type of the gender?")
        text.pack()
        gender_list = tk.Listbox(self)
        gender_list.pack()

        def get_gender():

            gender = gender_list.get("active")
            gender_label['text'] = "You selected: " + gender

        select_btn = tk.Button(self, text="Select",
                               command=get_gender)
        select_btn.pack()

        gender_label = tk.Label(self, text="")
        gender_label.pack()

        def getValues():
            stype = stype_label["text"].split(":")[-1].strip()
            team_type = team_type_label["text"].split(":")[-1].strip()
            gender = gender_label["text"].split(":")[-1].strip()
            team_type_list.delete(0, tk.END)
            gender_list.delete(0, tk.END)
            stype_label["text"] = ''
            team_type_label["text"] = ''
            gender_label['text'] = ''
            m.get_gold_medel_player(connection, cur, stype, team_type, gender, msg_final)


        # submit
        submit_btn = tk.Button(self, text="SUBMIT",
                               command=getValues)
        submit_btn.pack()

        msg_final = tk.StringVar()
        msgLabel = tk.Label(self, textvariable=msg_final)
        msgLabel.pack()


        def refresh():
            team_type_list.delete(0, tk.END)
            gender_list.delete(0, tk.END)
            stype_label["text"] = ''
            team_type_label["text"] = ''
            gender_label['text'] = ''

        refresh_button = tk.Button(self, text="refresh", command=refresh)
        refresh_button.pack()
        goBack = tk.Button(self, text="Back", command=lambda: controller.show_frame(0))
        quit_bt = tk.Button(self, text="Quit", command=self.quit)
        quit_bt.pack(side='bottom')
        goBack.pack(side='bottom')


class Option7(tk.Frame):
    '''
        Add a participation to the database
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Please fill the participation information", font=('Arial', 10))
        label.pack(pady=10, padx=10)

        # code for scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # pid
        text = tk.Label(self, text="What is the player's pid? It has to be greater than 0")
        text.pack()

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        pid_list = tk.Listbox(self, yscrollcommand=scrollbar.set)
        pid_list.pack()
        scrollbar.config(command=pid_list.yview)

        try:
            cur.execute('select player_id from player;')
            pids = map(str, sorted(list(map(lambda x: x[0], cur.fetchall()))))
            for pid in pids:
                pid_list.insert(tk.END, pid)
            connection.commit()
        except psycopg2.Error as e:
            connection.rollback()
            # msg_1.set(e.pgerror)

        def get_pid():
            pid_label['text'] = "You selected: " + pid_list.get("active")

        select_btn = tk.Button(self, text="Select",
                               command=get_pid)
        select_btn.pack()

        pid_label = tk.Label(self, text="")
        pid_label.pack()

        text = tk.Label(self, text="Please select the sports: ")
        text.pack()

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        sports_list = tk.Listbox(self, yscrollcommand=scrollbar.set, width = 50)
        sports_list.pack()
        scrollbar.config(command=pid_list.yview)

        try:
            cur.execute('select sports_id, stype, sname, team_type, gender, distance from sports;')
            sports = map(lambda x: map(str, x),cur.fetchall())
            for sport in sports:
                sports_list.insert(tk.END, " ".join(sport))
            connection.commit()
        except psycopg2.Error as e:
            connection.rollback()
            # msg_1.set(e.pgerror)

        def get_sport():
            sports_tuple = sports_list.get("active")
            sports_label['text'] = "You selected: " + sports_tuple
            try:
                # cur.execute('select match_id, match_type, location, match_date from matches where sports_id = ;')
                sports_id = int(sports_tuple.split()[0])
                cur.execute('select * from matches where sports_id = %s;', (sports_id, ))
                matches = map(lambda x: map(str, x), cur.fetchall())
                for match in matches:
                    matches_list.insert(tk.END, " ".join(match))
                connection.commit()
            except psycopg2.Error as e:
                connection.rollback()
                sports_label['text'] = "No match related to your selection."

        select_btn = tk.Button(self, text="Select", command=get_sport)
        select_btn.pack()

        sports_label = tk.Label(self, text="")
        sports_label.pack()


        text = tk.Label(self, text="Please select the match: ")
        text.pack()

        matches_list = tk.Listbox(self, width = 50)
        matches_list.pack()

        def get_matches():
            matches_label['text'] = "You selected: " + matches_list.get("active")

        select_btn = tk.Button(self, text="Select", command=get_matches)
        select_btn.pack()

        matches_label = tk.Label(self, text="")
        matches_label.pack()



        # input result:
        text = tk.Label(self, text="Please input the player's result(e.g. 23.4s):")
        text.pack()

        result_entry = tk.Entry(self)
        result_entry.pack()

        def getvalue():
            pid = int(pid_label['text'].split(":")[1].strip())
            match_id = int(matches_label['text'].split(":")[1].split()[0])
            result = result_entry.get()
            regex = r"[1-9]+[.]*[0-9]*[s]$"

            matches = re.match(regex, result)
            if not matches:
                msgLabel['text'] = "Please input the correct format"
                return
            try:
                # cur.execute('select match_id, match_type, location, match_date from matches where sports_id = ;')
                cur.execute('''
                select result, match_type from 
                    matches m inner join participate p on 
                    m.match_id = p.match_id 
                    where m.match_id = %s
                ;''', (match_id, ))
                result_tuples = cur.fetchall()
                ranking = 0
                medal = None
                if result_tuples:
                    match_type = result_tuples[0][1]
                    match_results = map(lambda x:float(re.sub('[^0-9.]','', x[0])), result_tuples)
                    numeric_result = float(re.sub('[^0-9.]', '', result))
                    match_results.append(numeric_result)
                    match_results = sorted(match_results)
                    ranking = match_results.index(numeric_result) + 1

                    if match_type == 'final' and ranking <= 3:
                        if ranking == 1: medal = 'gold'
                        elif ranking == 2: medal = 'silver'
                        elif ranking == 3: medal = 'bronze'
                else:
                    ranking = 1
                connection.commit()
            except Exception as e:
                connection.rollback()
                msgLabel['text'] = str(e)

            try:
                cur.execute("insert into participate values (%s, %s, %s, %s, %s);", (pid, match_id, result, ranking, medal, ))
                msgLabel['text'] = "Your processed result is: \n" + \
                        "player id: {}\n match_id: {}\n result: {}\n ranking: {}\n medal: {}" \
                        .format(pid, match_id, result, ranking, medal)
                connection.commit()
            except psycopg2.Error as e:
                connection.rollback()
                msgLabel['text'] = str(e)

            result_entry.delete(0, tk.END)
            matches_list.delete(0, tk.END)
            pid_label['text'] = ''
            sports_label['text'] = ''
            matches_label['text'] = ''

        # submit
        submit_btn = tk.Button(self, text="SUBMIT",
                               command=getvalue)
        submit_btn.pack()

        # success message
        msgLabel = tk.Label(self, text = '')
        msgLabel.pack()

        def refresh():
            result_entry.delete(0, tk.END)
            matches_list.delete(0, tk.END)
            pid_label['text'] = ''
            sports_label['text'] = ''
            matches_label['text'] = ''
            msgLabel['text'] = ''
        refresh_button = tk.Button(self, text="refresh", command=refresh)
        refresh_button.pack()
        goBack = tk.Button(self, text="Back", command=lambda: controller.show_frame(0))
        quit_bt = tk.Button(self, text="Quit", command=self.quit)
        quit_bt.pack(side='bottom')
        goBack.pack(side='bottom')

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
    print("Exiting program")
    sys.exit(exit_code)
