CREATE INDEX pcname ON player(cname);
DROP INDEX pcname;

-- Easier to run query update_country_medal. The index on country help associate the player
-- with the appropriate country to update the medal count for that country : 

-- Update country
--	set gold_number = 
--	(select sum(player.gold_number) from player
--	 where country.cname = player.cname
--	),
--	silver_number = 
--	(select sum(player.silver_number) from player
--	 where country.cname = player.cname
--	),
--	bronze_number = 
--	(select sum(player.bronze_number) from player
--	 where country.cname = player.cname
--	),
--	total_medal_number = 
--	(select sum(player.gold_number)+sum(player.silver_number)+sum(player.bronze_number) from player
--	 where country.cname = player.cname
--	);
-- In this query we want to update the medal count for countries. 
-- For each tuple in the country table we look for 
-- the players with the same country name, thus creating an index on 
-- cname of player makes it faster to find the associated players


CREATE INDEX goldplayer ON player(gold_number);
DROP INDEX goldplayer;

-- this will speed up all the execution of all queries that try to find data based on the gold medal attribute:
-- Here are a few queries used in our GUI that will be sped up:

--1) get_gold_medels_player:
--	select pname, gold_number from player
--        where player_id = any
--        (
--            select player_id from player
--            where gold_number > 0
--            intersect
--            select player_id from participate
--            where match_id = any
--            (
--                select match_id from matches
--                where sports_id = any
--                (
--                    select sports_id from sports
--                    where stype = %s and team_type = %s and gender = %s
--                )
--            )
-- 	    );

 
--2) female_player_with_most_gold_medals_in_country_with_most_gold_medals:
--	select pname, gold_number, cname from player
--        where cname in (select cname from country where gold_number = (
--                select max(gold_number) from country
--            )
--        )
--        and gender = 'Female'
--        and gold_number = (
--        select max(gold_number) from player
--            where gender = 'Female' and cname in
--            (select cname from country where gold_number = (
--                select max(gold_number) from country
--                )
--            )
--        );


--3) player_with_most_gold_medals: 
--	select pname, gold_number from player
--      where cname = %s
--      and gold_number = (
--            select max(gold_number) from player
--            where cname = %s
--            );'


