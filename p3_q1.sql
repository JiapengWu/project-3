

create or replace function Procedure_name(pCname Varchar(30), total int, gold int, silver int,bronze int) --([proc_parameter[,...]])          
returns setof country
As
$$
    select * from country
    where cname = pCname or bronze_number = bronze or total_medal_number = total
    	  or gold_number =  gold or silver_number = silver
$$ LANGUAGE SQL;

select * from Procedure_name('canada', 5, 3, 2 ,2);