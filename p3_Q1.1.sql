-- verfies if a country has the proper amount of total medals, gives a list of all the 
--country it beats in the olympics and prints a report of the percentage of medal type won
--still needs to include the use of a cursor ****

create OR REPLACE function Procedure_name(pCname Varchar(30), total int, gold int, silver int,bronze int,
                                        out most_of_one_type varchar(20), OUT gold_percentage decimal, OUT silver_percentage decimal, OUT bronze_percentage decimal)          
returns record as
$$
--DECLARE counter INTEGER := total_medal_number ; --medal counter
DECLARE verifier RECORD; -- hold record value
begin

      RAISE NOTICE '% beats :',pCname;
      FOR verifier IN SELECT cname,total_medal_number FROM country
        LOOP 
        if pCname = verifier.cname then
            if total != verifier.total_medal_number then
            RAISE NOTICE '*************** % doesnt this amount of medals ********************',pCname;
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
      RAISE NOTICE 'percentage of medal type won ';
      RAISE NOTICE '';

end; $$ 
LANGUAGE plpgsql;

--test case
select * from Procedure_name('Canada',3,1,2,0);





-- unfinished or not so relevant
-- |
-- |
-- V









-- function that return the country with the most medals from a list of countries ?


--
DECLARE cursor1 CURSOR 
FOR
      SELECT total_medal_number,gold_number,silver_number,bronze_number
      FROM country;
 
      --OPEN CURSOR.
      OPEN cursor1 
 
      --FETCH THE RECORD INTO THE VARIABLES.
      FETCH NEXT FROM cursor1 INTO
      @CustomerId, @Name, @Country;




--first attemp  at Q.1 
--using cursor (pointer to row, process one row at the time) are slow but bring interesting use


create procedure Procedure_name  
(cname Varchar(30), total int, gold int, silver int,bronze int) --([proc_parameter[,...]])          
As
Begin
    update country
    set (
    	cname = @cname,total_medal_number = @total,gold_number =  @gold,
    	silver_number = @silver, bronze_number = @bronze
    	)
    where country.cname = @cname 
end
;
--to execute procedure --Execute Procedure_name 003,�xyz�,27,1234567890
execute Procedure_name canada,0,0,0,0 ; 



--testcursor







--second attemps
declare @total int;
declare @cname nvarchar(30);

declare country_cursor for
select cname,total_medal_number from country
where total_medal_number > 5

open country_cursor

fetch next from country_cursor into @cname,@total

while(@@fetch_status = 0) -- while cursor has row to process
begin
	
	print 'country of '+ cname+ ' has '+ cast(@totalt as nvarchar(5)) + ' medals'
	
	
	fetch next from country_cursor into @cname,@total
end 

close country_cursor

--ibm example 

CREATE procedure sum_salaries(OUT sum INTEGER) 
  LANGUAGE SQL
  BEGIN
    DECLARE p_sum INTEGER;
    DECLARE p_sal INTEGER;
    DECLARE c CURSOR FOR SELECT SALARY FROM EMPLOYEE;
    DECLARE SQLSTATE CHAR(5) DEFAULT '00000';
 
     SET p_sum = 0;

     OPEN c;

     FETCH FROM c INTO p_sal;

     WHILE(SQLSTATE = '00000') DO
        SET p_sum = p_sum + p_sal;
        FETCH FROM c INTO p_sal; 
     END WHILE;

     CLOSE c;

     SET sum = p_sum;

  END%;
  --
CREATE PROCEDURE MIN_SALARY (IN deptnumber SMALLINT, IN minsal DOUBLE)
LANGUAGE SQL
BEGIN
DECLARE v_salary DOUBLE;
DECLARE v_id SMALLINT;
DECLARE at_end INT DEFAULT 0;
DECLARE not_found CONDITION FOR SQLSTATE '02000';
DECLARE C1 CURSOR FOR
SELECT id, salary FROM staff WHERE did = deptnumber;
DECLARE CONTINUE HANDLER FOR not_found SET at_end = 1;
OPEN C1;
FETCH C1 INTO v_id, v_salary;
WHILE at_end = 0 DO
IF (v_salary < minsal)
THEN UPDATE staff SET salary = minsal WHERE id = v_id;
END IF;
FETCH C1 INTO v_id, v_salary;
END WHILE;
CLOSE C1;
END