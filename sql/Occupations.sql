/*
Enter your query here.
*/
SET @r1=0, @r2=0, @r3=0, @r4=0;
SELECT  Min(doctor), min(professor), min(singer), min(actor) from
 (select case occupation  when 'doctor' then @r1:=@r1+1
                          when 'professor' then @r2:=@r2+1
                          when 'singer' then @r3:=@r3+1
                          when 'actor' then @r4:=@r4+1 end
                          as rowline,
                          case when occupation = 'doctor' then name end as doctor,
                          case when occupation = 'professor' then name end as professor,
                          case when occupation = 'singer' then name end as singer,
                          case when occupation = 'actor' then name end as actor
                          from occupations  order by name)
                          as t
                          group by rowline;