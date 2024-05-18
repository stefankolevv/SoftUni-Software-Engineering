CREATE VIEW
	view_addresses
AS
SELECT
	CONCAT(
		e.first_name,
		' ',
		e.last_name
	) AS full_name,
	e.department_id,
	CONCAT(
		a.number,
		' ',
		a.street
	) AS address
FROM 
	employees AS e, addresses as a
WHERE
	a.id = e.address_id
ORDER BY
	address;