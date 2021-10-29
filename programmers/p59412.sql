select HOUR, count(HOUR) as COUNT
from (select HOUR(DATETIME) as HOUR from ANIMAL_OUTS) as sub
group by HOUR
having HOUR>=9 and HOUR<=19
order by HOUR