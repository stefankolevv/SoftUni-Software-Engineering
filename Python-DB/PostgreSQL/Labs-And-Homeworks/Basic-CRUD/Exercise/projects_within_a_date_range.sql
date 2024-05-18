SELECT
	name,
	start_date,
	end_date
FROM
	projects
WHERE
	start_date >= '2016-06-01 07:00:00' -- yyyy-mm-dd hh:mm:ss
		AND
	end_date < '2023-06-04 00:00:00'
ORDER BY
	start_date;