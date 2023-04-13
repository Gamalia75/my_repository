-- 1.	Напишіть запит, щоб отримати всі відомості про співробітників із таблиці employee упорядковано за іменами за зростанням.

select * from employees order by FIRST_NAME, LAST_NAME;

--  2.	Напишіть запит, щоб отримати імена, зарплату та податки усіх спiвробітників податки (розраховується як 15% від зарплати)

select FIRST_NAME, LAST_NAME, SALARY, SALARY*0.15 as TAXES from employees order by FIRST_NAME, LAST_NAME;

-- 3.	Напишіть запит, щоб отримати загальну суму заробітну плату всіх співробітників.

select sum(SALARY) as Total_Salary from employees;

-- 4.	Напишіть запит для отримання максимальної та мінімальної зарплати працівників.

select min(SALARY) as Min_Salary, max(SALARY) as Max_Salary from employees;

-- 5.	Напишіть запит, щоб отримати середню заробітну плату та кількість працівників у таблиці employee.

select avg(SALARY) as Avg_Salary, count(EMPLOYEE_ID) as Employee_Qty from employees;
