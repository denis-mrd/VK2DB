select city, count(*)  as quantity
from friends
group by city
order by quantity desc;


select YEAR(convert(date, bdate, 104)) as year, count(*)  as quantity
from friends 
group by YEAR(convert(date, bdate, 104))
order by quantity desc;

SELECT
	count(*) as quantity,
    CASE WHEN sex=1 THEN '������� ���'
         WHEN sex=2 THEN '������� ���'
         ELSE '��� �� ������'
		END
    FROM friends
group by sex
order by quantity desc;