SELECT
    first_name,
    last_name,
    extract('year' FROM born) AS year
FROM authors