#!/usr/bin/python
import psycopg2
import modules as m

config = "user='cs421g19' host='comp421.cs.mcgill.ca' dbname='cs421' password='Pmdd0301'"

connection = psycopg2.connect(config)
cur = connection.cursor()

option = input("select 1 to execute query 1\nselect 2 to execute query 2\nselect 3 to execute query 3\nselect 4 to execute query 4\nselect 5 to execute query 5")

# Redirects to option that user chose
if(option == 1) option_1
elif (option == 2) option_2
elif (option == 3) option_3
elif (option == 4) option_4
elif (option == 5) option_5
else print 'You did not choose a correct option.'

# The add single player option
def option_1() :
    # Input player ID
    pid = input("What is the player's pid? It has to be greater than 0")
    if (pid < 0) raise PIDError('Pid less than 0')

    # Input name
    try:
        name = raw_input("What is the player's name?")
    except ValueError:
        raise NameError("Invalid name")
    # Gender
    gender = raw_input("What is the player's gender") 
    if (gender != "Male" and gender != Female) raise GenderError('Unvalid gender')

    # What is the nationality
    try:
        nationality = raw_input("What is the player's country")
    except ValueError:
        raise NatError("Invalid nationality")

    m.add_single_player(cur, pid, name, gender, nationality)

# The find a player from a country with the most gold medals option
def option_1() :  

    # What is the country
    try:
        country = raw_input("What is the player's country")
    except ValueError:
        raise CountryError("Invalid country")

    m.player_with_most_gold_medals(cur, country)

connection.close()


# import psycopg2
# conn = psycopg2.connect("user='cs421g19' host='comp421.cs.mcgill.ca' dbname='cs421' password='Pmdd0301'")
# cursor = conn.cursor()
# conn.execute('SELECT %s FROM %s', ('*','player')) # SQL, first argument statement, second argument tuple of % substitutions Python string style (do NOT use ('...%s...' % variable)))
# conn.commit() # confirm changes to database, not needed for pure select
# conn.fetch() # one row
# conn.fetchmany(N) # N rows
# cursor.fetchall() # all rows into tuple of tuple (rows of columns)
# conn.close() # close connection very important