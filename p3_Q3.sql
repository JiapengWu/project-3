CREATE INDEX pcname ON player(cname);
DROP INDEX pcname;

-- easier to run query update_country_medal: 

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

-- this will speed up all the queries that try to find either the male or female players that won 
-- a gold medal
-- e.g. player_with_most_gold_medals; 
--      female_player_with_most_gold_medals_in_country_with_most_gold_medals;
--      get_gold_medel_player
