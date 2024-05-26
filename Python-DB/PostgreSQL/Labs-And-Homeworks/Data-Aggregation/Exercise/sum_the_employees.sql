SELECT
    COUNT(CASE department_id WHEN 1 THEN 1 ELSE NULL end) "Engineering",
    COUNT(CASE department_id WHEN 2 THEN 1 ELSE NULL end) "Tool Design",
    COUNT(CASE department_id WHEN 3 THEN 1 ELSE NULL end) "Sales",
    COUNT(CASE department_id WHEN 4 THEN 1 ELSE NULL end) "Marketing",
    COUNT(CASE department_id WHEN 5 THEN 1 ELSE NULL end) "Purchasing",
    COUNT(CASE department_id WHEN 6 THEN 1 ELSE NULL end) "Research and Development",
    COUNT(CASE department_id WHEN 7 THEN 1 ELSE NULL end) "Production"
FROM employees