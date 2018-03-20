# write functions that perform queries and modification here


# Add one player
# return 1 if successful
# return 0 if failure
def add_single_player(cur, pid, name, gender, nationality):
    try:
        cur.execute( "insert into  player values ('%s', '%s', '%s', '%s', 0, 0, 0);" , (pid, name, gender, nationality))
    except:
        return 0;
    return 1;


# find the Canadian who has won the most gold medals

def player_with_most_gold_medals(cur, country):
        cur.execute('''select pname, gold_number from player
            where cname = %s
            and gold_number = (
                select max(gold_number) from player
                where cname = %s
                );''',(country, country,))
        return cur.fetchall()

def add_single_player(cur, pid, name, gender, nationality):
    try:
        cur.execute( "insert into  player values ('%s', '%s', '%s', '%s', 0, 0, 0);" , (pid, name, gender, nationality))
    except:
        return 0;
    return 1;

# Find female with the most gold medals from country with most total medals

def player_with_most_gold_medals(cur):
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

