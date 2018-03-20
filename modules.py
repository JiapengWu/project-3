# write functions that perform queries and modification here
import psycopg2
def doQuery(cur) :

    cur.execute( "SELECT cname, total_medal_number FROM country" )

    for firstname, lastname in cur.fetchall() :
        print firstname, lastname