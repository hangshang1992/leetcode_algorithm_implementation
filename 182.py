# Write your MySQL query statement below
select Email 
from (select Email, count(Id) as num from Person group by Email) as a
where a.num >= 2
