# write functions that perform queries and modification here

import psycopg2

# Add one player
def add_single_player(conn, cur, pid, name, gender, nationality, msg):
    try:
        cur.execute( "insert into  player values (%s, %s, %s, %s, 0, 0, 0);" , (pid, name, gender, nationality))
        conn.commit() #connection must commit all executions done (save changes)
        #cursor will return to initial  position automatically
        msg.set("Player added successfully.")
    except psycopg2.Error as e:
        conn.rollback() #if error cursor is stuck so ned to manually reset connection and cursor to execute next statement 
        msg.set(e.pgerror)


# find the Canadian who has won the most gold medals

def player_with_most_gold_medals(cur, country):
    cur.execute('''select pname, gold_number from player
        where cname = %s
        and gold_number = (
            select max(gold_number) from player
            where cname = %s
            );''',(country, country,))
    return cur.fetchall()


# Find female with the most gold medals from country with most total medals

def female_player_with_most_gold_medals_in_country_with_most_gold_medals(cur):
    cur.execute('''select pname, gold_number from player
    where cname in (select cname from country where gold_number = (
                select max(gold_number) from country
                )
            )
        and gender = 'Female'
        and gold_number = (
        select max(gold_number) from player
            where gender = 'Female' and cname in
            (select cname from country where gold_number = (
                select max(gold_number) from country
                )
            )
        );''')
    return cur.fetchall()


# update give a medal to each player who won 1st, 2nd or 3rd place in  a 'finals' match
# if the player won more than one medal (participated in multiple matches) give him the right number of medals
def update_player_medal(cur):
    cur.execute('''do $$
          declare
            arow record;
            BEGIN
                FOR arow IN SELECT player_id FROM (
                    SELECT player_id FROM participate p
                    right JOIN matches ON matches.match_type = 'final' and p.match_id = matches.match_id
                    ) s
                LOOP
                    UPDATE player
                        SET gold_number = (select count(*) from participate p where ranking = 1 and p.player_id = arow.player_id)
                        ,silver_number = (select count(*) from participate p where ranking = 2 and p.player_id = arow.player_id)
                        ,bronze_number = (select count(*) from participate p where ranking = 3 and p.player_id = arow.player_id)
                        where player_id = arow.player_id;
                END LOOP;
            END; $$''')


# -- get the number of medals from each player of same country
# -- add it to each respective medal count of that country
# -- then calculate the total number of medals for that country
def update_country_medal(cur):
    cur.execute('''Update country
        set gold_number = 
        (select sum(player.gold_number) from player
         where country.cname = player.cname
        ),
        silver_number = 
        (select sum(player.silver_number) from player
         where country.cname = player.cname
        ),
        bronze_number = 
        (select sum(player.bronze_number) from player
         where country.cname = player.cname
        ),
        total_medal_number = 
        (select sum(player.gold_number)+sum(player.silver_number)+sum(player.bronze_number) from player
         where country.cname = player.cname
        );''')

# Find all player female player who got gold and participate in a swimming match of type single
def get_gold_medel_player(cur, stype, team_type, gender):
    cur.execute('''
        select pname from player
        where player_id = any
        (
            select player_id from player
            where gold_number > 0
            intersect
            select player_id from participate
            where match_id = any
            (
                select match_id from matches
                where sports_id = any
                (
                    select sports_id from sports
                    where stype = %s and team_type = %s and gender = %s
                )
            )
 	    );''',(stype, team_type, gender))
    return cur.fetchall()
