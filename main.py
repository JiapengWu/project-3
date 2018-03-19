#!/usr/bin/python
import psycopg2
import modules as m

config = "user='cs421g19' host='comp421.cs.mcgill.ca' dbname='cs421' password='Pmdd0301'"

connection = psycopg2.connect(config)
cur = connection.cursor()
m.doQuery(connection)
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