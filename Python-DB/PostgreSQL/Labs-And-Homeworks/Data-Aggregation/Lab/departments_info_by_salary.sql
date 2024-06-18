SELECT
    department_id,
    count(salary)
FROM employees
GROUP BY department_id
ORDER BY department_id