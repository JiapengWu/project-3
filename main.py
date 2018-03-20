#!/usr/bin/python
import modules as m
import psycopg2
import logging

def option_1(cur):
    # Input player ID
    while True:
        pid = input("What is the player's pid? It has to be greater than 0")
        if (pid < 0):
            print('Pid less than 0')
            continue
        # Input name
        try:
            name = raw_input("What is the player's name?")
        except ValueError:
            print("Invalid name")
            continue
        # Gender
        gender = raw_input("What is the player's gender(Male or Female)")
        if (gender != "Male" and gender != 'Female'):
            print('Invalid input')
            continue
        # What is the nationality
        try:
            nationality = raw_input("What is the player's country")
        except ValueError:
            print("Invalid nationality")
            continue
        try:
            m.add_single_player(cur, pid, name, gender, nationality)
            logging.INFO("Successful.")
            break

        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)

def main():
    config = "user='cs421g19' host='comp421.cs.mcgill.ca' dbname='cs421' password='Pmdd0301'"

    connection = psycopg2.connect(config)
    cur = connection.cursor()

    option = input(
        '''select 1 to execute query 1
         select 2 to execute query 2
         select 3 to execute query 3
         select 4 to execute query 4
         select 5 to quit
        ''')

    # Redirects to option that user chose
    while True:
        if(option == 1):
            option_1(cur)
        elif (option == 2):
            pass
        elif (option == 3):
            pass
        elif (option == 4):
            pass
        elif (option == 5):
            break
        else:
            logging.WARNING('You did not choose a correct option.')
    connection.close()
    # The add single player option


main()


