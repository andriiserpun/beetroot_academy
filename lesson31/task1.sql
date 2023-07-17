select employees.first_name, employees.last_name, employees.department_id, department.department_name
from employees, department
join departments on employees.department_id = departments.department_id;

select employees.first_name, employees.last_name, department.department_name, locations.city, locations.state_province
from employees, department
join departments on employees.department_id = departments.department_id
join locations on departments.location_id = locations.location_id;

select employees.first_name, employees.last_name, employees.department_id, department.department_name
from employees, department
join departments on employees.department_id = departments.department_id
where departments.department_id in (80, 40);

select department.department_id, department.department_name
from department
left join employees on department.department_id = employees.department_id
where employees.department_id is null;

select e.last_name as employeelast_name, m.last_name as managerlast_name
from employees e
left join employees m on e.manager_id = m.employee_id;

select jobs.job_title, employees.first_name, employees.last_name, jobs.max_salary - employees.salary as salary_difference
from jobs
join employees on jobs.job_id = employees.job_id;

select jobs.job_title, avg(employees.salary) as average_salary
from jobs
join employees on jobs.job_id = employees.job_id
group by jobs.job_title;

select employees.last_name, employees.salary
from employees
join departments on employees.department_id = departments.department_id
join locations on departments.location_id = locations.location_id
where locations.city = 'london';

select department.department_name, count(*) as employee_count
from department
join employees on department.department_id = employees.department_id
group by department.department_name;