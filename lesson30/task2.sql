select first_name as "First Name", last_name as "Last Name" from employees;
select distinct department_id from employees;
select * from employees order by last_name desc;
select first_name as "First Name", last_name as"Last Name", salary as salary, 0.12 * salary as PF from employees;
select max(salary) as max_salary, min(salary) as min_salary from employees;
select first_name, last_name, round(salary/12, 2) as monthly_salary from employees;