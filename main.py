#!/usr/bin/python
import modules as m
import psycopg2
import logging

def option_1(cur):
    # Input player ID
    while True:
        pid = input("What is the player's pid? It has to be greater than 0\n")
        if (pid < 0):
            print('Pid less than 0')
            continue
        # Input name
        try:
            name = raw_input("What is the player's name?\n")
        except ValueError:
            print("Invalid name")
            continue
        # Gender
        gender = raw_input("What is the player's gender(Male or Female)?\n")
        if (gender != "Male" and gender != 'Female'):
            print('Invalid input')
            continue
        # What is the nationality
        try:
            nationality = raw_input("What is the player's country\n")
        except ValueError:
            print("Invalid nationality")
            continue
        try:
            m.add_single_player(cur, pid, name, gender, nationality)
            print("Successful.")
            break

        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)

def option_2(cur):
    while True:
        try:
            country = raw_input("What is the player's country\n")
            result = m.player_with_most_gold_medals(cur, country)
            if result:
                print("The player who has won the most gold medals in {} is: {}, the gold number is: {}"
                      .format(country,
                              (', ').join(map(lambda x:x[0],result)),
                              (', ').join(map(str,map(lambda x:x[1],result)))))
                break
            else:
                print("Country does not exit in the database.")
        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
            continue

def option_3(cur):
    try:
        result = m.female_player_with_most_gold_medals_in_country_with_most_gold_medals(cur)
        print(result)
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

def option_4(cur):
    try:
        m.update_player_medal(cur)
        print("Successful.")
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

def option_5(cur):
    try:
        m.update_country_medal(cur)
        print("Successful.")
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

def option_6(cur):
    while True:
        try:
            stype = raw_input("What is the type of the sports(Swimming, Athletics)?\n")
        except ValueError:
            print("Invalid stype")

        try:
            cur.execute('select team_type from sports where stype = %s',(stype, ))
            team_types = cur.fetchall()
        except:
            print("Sports name is not in the database")
            continue
        team_type = raw_input("What is the type of the team type({})?\n".format((', ').join(set(map(lambda x:x[0],team_types)))))

        # try:
        #     cur.execute("select gender from sports where stype = %s, team_type = %s",(stype, team_type, ))
        #     genders = cur.fetchall()
        # except:
        #     print("Team-type is not in the database")
        #     continue
        cur.execute("select gender from sports where stype = %s and team_type = %s", (stype, team_type,))
        genders = cur.fetchall()
        gender = raw_input("What is the type of the gender({})?\n".format((', ').join(set(map(lambda x:x[0],genders)))))

        try:
            result = m.get_gold_medel_player(cur, stype, team_type, gender)
            if result:
                print("The golder winners are: {}".format((', ').join(map(lambda x:x[0],result))))
                print("The gold numbers are: {}".format((', ').join(map(lambda x: x[1],result))))
                break
            else:
                print("No result")
        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)


def main():
    config = "user='cs421g19' host='comp421.cs.mcgill.ca' dbname='cs421' password='Pmdd0301'"

    connection = psycopg2.connect(config)
    cur = connection.cursor()
    while True:
        option = input(
        'select 1 to add single player \
        \nselect 2 to find the players who have won the most gold medals given the country \
        \nselect 3 to find female with the most gold medals from country with most total medals \
        \nselect 4 to update the medal number of each player who participated in  a \'finals\' match \
        \nselect 5 to update the total medal number for each country based on the player medal numbers \
        \nselect 6 to find all player that get gold medal given the name of the sport \
        \nselect 7 to quit')

    # Redirects to option that user chose

        if(option == 1):
            option_1(cur)
        elif (option == 2):
            option_2(cur)
        elif (option == 3):
            option_3(cur)
        elif (option == 4):
            option_4(cur)
        elif (option == 5):
            option_5(cur)
        elif (option == 6):
            option_6(cur)
        elif (option == 7):
            break
        else:
            logging.WARNING('You did not choose a correct option.')

    connection.close()
    # The add single player option


main()


