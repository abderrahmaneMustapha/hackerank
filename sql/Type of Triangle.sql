SELECT
    CASE
    WHEN (a+b)> c and (a+c)>b and (b+c) >a then 
    CASE
    WHEN (a=b) and (a=c) and (b=c) then "Equilateral"
    WHEN (a=b) or (b=c) or (c=a)then  "Isosceles"
    ELSE "Scalene"
    END
ELSE  "Not A Triangle"
END
FROM TRIANGLES