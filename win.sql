select city_title, count(*)  as quantity 
from friends 
group by city_title 
order by quantity desc


select YEAR(try_convert(date, bdate, 104)) as year, count(*)  as quantity 
from friends 
group by YEAR(try_convert(date, bdate, 104)) 
order by quantity desc

select sex, count(*) as quantity 
from friends 
group by sex
order by quantity desc

--select * from friends