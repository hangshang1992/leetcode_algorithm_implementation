# Write your MySQL query statement below
select T.id,
if(isnull(T.p_id), 'Root', if(T.id in (select p_id from tree), 'Inner', 'Leaf')) Type
from tree T
