# Write your MySQL query statement below
Select max(Salary) as SecondHighestSalary from Employee
where Salary < (Select MAX(Salary) from Employee)
