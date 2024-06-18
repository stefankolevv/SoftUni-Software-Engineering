SELECT username, gender, age
FROM accounts
WHERE age >= 18 AND LENGTH(username) > 9
ORDER BY age DESC, username ASC; -- Age descending ->> username ascending.