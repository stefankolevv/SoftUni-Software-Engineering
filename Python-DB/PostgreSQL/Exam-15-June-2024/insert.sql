INSERT INTO addresses (street, town, country, account_id)
SELECT username, password, ip, age
FROM accounts
WHERE gender = 'F'; -- For accs identified as F = female gender.