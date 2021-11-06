select
    in_id as ANIMAL_ID, in_name as NAME
from
    (select ANIMAL_ID as in_id, NAME as in_name, DATETIME as in_date from ANIMAL_INS) as ins,
    (select ANIMAL_ID as out_id, NAME as out_name, DATETIME as out_date from ANIMAL_OUTS) as outs
where in_date > out_date and in_id = out_id
order by in_date