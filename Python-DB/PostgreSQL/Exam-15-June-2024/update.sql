UPDATE addresses
SET country = 'Blocked'
WHERE country LIKE 'B%'; -- Changing from 'B' to 'Blocked' as required.

UPDATE addresses
SET country = 'Test'
WHERE country LIKE 'T%';

UPDATE addresses
SET country = 'In Progress'
WHERE country LIKE 'P%';