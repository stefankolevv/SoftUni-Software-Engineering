SELECT
    id,
    first_name,
    last_name,
    job_title,
    department_id,
    salary
FROM employees
WHERE department_id=4 and salary>=1000