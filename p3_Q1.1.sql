-- verfies if a country has the proper amount of total medals (not g/s/b), gives a list of all the 
--country it beats in the olympics and prints a report of the percentage of medal type won ex: 0.1 gold| 0.5 silver | 0.4 bronze
-- using a cursor to find the best gold win ratio and the one that owns it between all countries
--could be separated between its different uses, but kept toguether for conveniance

create OR REPLACE function medal_verifier(pCname Varchar(30), total int, gold int, silver int,bronze int,
                                        out most_of_one_type varchar(20), OUT gold_percentage decimal, OUT silver_percentage decimal, OUT bronze_percentage decimal)          
returns record as
$$
--DECLARE counter INTEGER := total_medal_number ; --medal counter
DECLARE     
    verifier RECORD; -- hold record value
    max_gold_ratio int  = 0 ; -- hold best gold ratio
    max_cname Varchar(40)  = 'everyone, no one got any gold' ; -- country that hold it
    record_country record ; -- declare record holer
    cur_country CURSOR -- declare cursor
        for select * from country ;
begin

      RAISE NOTICE '% beats :',pCname;
      FOR verifier IN SELECT cname,total_medal_number FROM country
        LOOP 
        if pCname = verifier.cname then
            if total != verifier.total_medal_number then
            RAISE NOTICE '*************** % doesnt have this amount of medals ********************',pCname;
            end if;
        elsif total > verifier.total_medal_number then 
            RAISE NOTICE '%', verifier.cname;
        end if;
      END LOOP;

      -- check which type has the most medals
      IF gold > silver and gold > bronze THEN
      most_of_one_type :='gold';

      ELSIF silver > gold and silver > bronze THEN
      most_of_one_type := 'silver';

      ELSE
      most_of_one_type := 'bronze';
      END IF;

       
      gold_percentage := cast (gold as float) / total ;
      silver_percentage := cast (silver as float) / total ;
      bronze_percentage := cast (bronze as float) / total ;
      
      RAISE NOTICE '';
      RAISE NOTICE '*procedure completed*';

      RAISE NOTICE '';



    OPEN cur_country;
 
    LOOP
    -- fetch row into the film
      FETCH cur_country INTO record_country;
    -- exit when no more row to fetch
      EXIT WHEN NOT FOUND;
        if  record_country.total_medal_number != 0 and max_gold_ratio < cast (record_country.gold_number as float) / record_country.total_medal_number then
            max_gold_ratio := cast (record_country.gold_number as float) / record_country.total_medal_number ;
            max_cname := record_country.cname ;
        end if ;
    END LOOP;
  
    RAISE NOTICE 'the best gold win ratio is : % by %', max_gold_ratio, max_cname;
    RAISE NOTICE '';
   -- Close the cursor
    CLOSE cur_country;

      RAISE NOTICE 'percentage of medal type won ';
      RAISE NOTICE '';



end; $$ 
LANGUAGE plpgsql;

--test case
select * from medal_verifier('Canada',4,1,3,0);


