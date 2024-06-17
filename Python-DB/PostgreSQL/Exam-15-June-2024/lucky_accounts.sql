SELECT a.id || ' ' || a.username AS id_username, a.email
-- || ' ' || - Concatenate strings w/ a space between id and username.
FROM accounts a
JOIN accounts_photos ap ON a.id = ap.account_id
JOIN photos p ON ap.photo_id = p.id
WHERE a.id = p.id
ORDER BY a.id;