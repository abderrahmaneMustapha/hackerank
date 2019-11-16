SELECT ROUND(S.LAT_N,4) FROM  STATION S where 
(select @a := count(LAT_N) from station where LAT_N < S.LAT_N ) = (select @b :=count(LAT_N) from station 
where LAT_N > S.LAT_N);
