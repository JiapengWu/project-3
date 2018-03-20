#!/usr/bin/python
import modules as m
import psycopg2

config = "user='cs421g19' host='comp421.cs.mcgill.ca' dbname='cs421' password='Pmdd0301'"

connection = psycopg2.connect(config)
cur = connection.cursor()

#pick_option()
# Function that continues until you pick a valid option
def pick_option() :
    option = input("select 1 to execute query 1\nselect 2 to execute query 2\nselect 3 to execute query 3\nselect 4 to execute query 4\nselect 5 to execute query 5")

    # Redirects to option that user chose
    if(option == 1) : option_1()
    elif (option == 2) : option_2()
    elif (option == 3) : option_3()
    elif (option == 4) : option_4()
    elif (option == 5) : option_5()
    else :
        print 'You did not choose a correct option.'
        pick_option()

# The add single player option
def option_1() :
    # Input player ID
    pid = input("What is the player's pid? It has to be greater than 0")

    # Input name
    name = raw_input("What is the player's name?")

    # Gender
    gender = raw_input("What is the player's gender") 
    if (gender != "Male" and gender != "Female") : raise GenderError('Invalid gender')

    # What is the nationality
    nationality = raw_input("What is the player's country")

    # Try to call add_single_player. If SQL returns an exception, then print the message and let the user try again
    try:
        m.add_single_player(cur, pid, name, gender, nationality)
    except Exception as e :
        print e.message
        option_1()

# Find the player(s) from a country with the most gold medals option
def option_2() :

    # What is the country
    country = raw_input("What is the player's country")

    # Try to call player_with_most_gold_medals. If SQL returns an exception, then print the message and let the user try again
    try:
        m.player_with_most_gold_medals(cur, country)
    except Exception as e :
        print e.message
        option_2()

# Find the female(s) with the most gold medals option
def option_3() :

    # Try to call player_with_most_gold_medals. If SQL returns an exception, then print the message and let the user try again
    try:
        m.player_with_most_gold_medals(cur)
    except Exception as e :
        print e.message
        option_3()

def option_4() :
    print 'Option 4 not done yet'

def option_5() :
    print 'Option 5 not done yet'