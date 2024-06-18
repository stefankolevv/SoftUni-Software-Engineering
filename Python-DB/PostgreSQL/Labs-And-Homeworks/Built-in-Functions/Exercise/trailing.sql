SELECT
	continent_name,
	TRIM(TRAILING FROM continent_name) AS "trim"
FROM
	continents;