SELECT 
	MIN(average_area) AS min_average_area
FROM (
	SELECT
		AVG(area_in_sq_km) AS average_area
	FROM 
		countries 
	GROUP BY
		continent_code
) AS min_average_area