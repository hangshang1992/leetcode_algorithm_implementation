# Write your MySQL query statement below
select a.Score, count(b.Score) as Rank
from Scores as a, 
(select distinct Score from Scores) as b
where a.Score <= b.Score
group by a.Id
order by a.Score desc
