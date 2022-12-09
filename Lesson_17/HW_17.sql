# 1.	Напишіть запит, щоб перерахувати кількість вакансій, доступних у таблиці employee.
select count(distinct(JOB_ID)) as Qty_jobs from employees;

# 2.	Напишіть запит, щоб отримати середню заробітну плату та кількість працівників відділу 90.
select count(EMPLOYEE_ID) as Qty_workers, avg(SALARY) as Avg_salary from employees where DEPARTMENT_ID=90;

# 3.	Напишіть запит, щоб отримати кількість працівників з тією самою роботою.
select JOB_ID, count(JOB_ID) as Qty_workers from employees group by JOB_ID;

# 4.	Напишіть запит, щоб знайти ім'я (ім'я, прізвище),  код і повну назву ВІДДІЛУ.
SELECT first_name, last_name, department_id, department_name
FROM employees
LEFT JOIN departments USING (department_id);

# 5.	Напишіть запит, щоб знайти ім'я (ім'я, прізвище), роботу, ідентифікатор відділу
# та імена співробітників, які працюють у Лондоні.
select FIRST_NAME, LAST_NAME, JOB_ID, d.DEPARTMENT_ID, DEPARTMENT_NAME 
from employees e 
left join departments d on e.DEPARTMENT_ID = d.DEPARTMENT_ID 
left join locations l on l.LOCATION_ID = d.LOCATION_ID
where CITY = "London";