Basic Select Statement

1. SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees

2. SELECT department_id FROM employees GROUP BY department_id 

3. SELECT first_name, last_name FROM employees ORDER BY first_name DESC

4. SELECT first_name, last_name, salary, salary*0.15 AS "PF" FROM employees

5. SELECT employee_id, first_name, last_name, salary FROM employees ORDER BY salary ASC

6. SELECT sum(salary) FROM employees

7. SELECT min(salary), max(salary) FROM employees

8. SELECT avg(salary) FROM employees

9. SELECT count(employee_id) FROM employees

10. SELECT upper(first_name) FROM employees

11. SELECT left(first_name, 3) FROM employees

12. SELECT CONCAT(first_name, ' ', last_name) AS "Full Name" FROM employees

13. SELECT first_name, last_name, length(CONCAT(first_name, last_name)) AS "Full Name" FROM employees

14. SELECT * FROM employees WHERE first_name ~ '[0-9]'

15. SELECT * FROM employees LIMIT 10


RESTRICTING AND SORTING
1. SELECT first_name, last_name, salary FROM employees WHERE salary BETWEEN '10000' AND '15000'

2. SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN '01/01/1987' AND '31/12/1987'

3. SELECT first_name, last_name FROM employees WHERE first_name LIKE '%c%' AND first_name LIKE '%e%'

4. SELECT first_name, last_name, job_title, salary 
FROM employees
JOIN jobs
ON employees.job_id = jobs.job_id 
WHERE job_title 
NOT IN ('Programmer', 'Shipping Clerk') 
AND salary NOT IN ('4500', '10000', '15000')

5. SELECT last_name FROM employees WHERE length(last_name) = 6

6. SELECT last_name FROM employees WHERE position('e' in last_name) = 3

7. SELECT distinct job_title 
FROM employees 
JOIN jobs 
ON employees.job_id = jobs.job_id

8. SELECT * FROM employees 
WHERE upper(last_name) IN ('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD')