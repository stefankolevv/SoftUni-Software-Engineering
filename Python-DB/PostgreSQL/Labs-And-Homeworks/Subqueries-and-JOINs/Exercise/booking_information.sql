SELECT 
	b.booking_id,
	a.name AS apartment_owner,
	a.apartment_id,
	c.first_name || ' ' || c.last_name AS customer_name
FROM
	bookings AS b
FULL JOIN
	apartments AS a
USING 
	(booking_id)
FULL JOIN
	customers AS c
USING 
	(customer_id)
ORDER BY
	b.booking_id,
	apartment_owner,
	customer_name;