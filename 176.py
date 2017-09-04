# Write your MySQL query statement below
Select max(Salary) from Employee
where Salary < (Select MAX(Salary) from Employee)
