CREATE INDEX pcname ON player(cname);
DROP INDEX pcname;

-- easier to run query update_country_medal: Faster to find the players associated 
-- with the country for which we want to update the medal count

CREATE INDEX goldplayer ON player(gold_number);
DROP INDEX goldplayer;

-- this will speed up all the queries that try to find either the male or female players that won 
-- a gold medal
-- e.g. player_with_most_gold_medals; 
--      female_player_with_most_gold_medals_in_country_with_most_gold_medals;
--      get_gold_medel_player