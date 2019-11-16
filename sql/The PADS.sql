SELECT concat(name,"(",left(occupation,1),")") FROM OCCUPATIONS
ORDER BY name ;

SELECT concat("There are a total of ", count(occupation), " ",LOWER(occupation), "s.") FROM OCCUPATIONS
GROUP BY  occupation
ORDER BY  count(occupation) asc, left(occupation,1)  asc 