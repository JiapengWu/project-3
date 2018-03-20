# write functions that perform queries and modification here


# Add one player
# return 1 if successful
# return 0 if failure
def add_single_player(cur, pid, name, gender, nationality) :
    try:
        cur.execute( "insert into  player values ('%s', '%s', '%s', '%s', 0, 0, 0);" , (pid, name, gender, nationality))
    except:
        return 0;
    return 1;


# find the Canadian who has won the most gold medals

def player_with_most_gold_medals(cur, country):
    try:
        cur.execute('''select pname, gold_number from player
        where cname = '%s'
        and gold_number = (
            select max(gold_number) from player
            where cname = '%s'
            );''',(country, country))
    except:
        return 0
    return 1
