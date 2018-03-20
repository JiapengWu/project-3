import modules as m
import psycopg2

config = "user='cs421g19' host='comp421.cs.mcgill.ca' dbname='cs421' password='Pmdd0301'"

connection = psycopg2.connect(config)
cur = connection.cursor()

m.add_single_player(cur, 10000, "", "", "China")

connection.close()