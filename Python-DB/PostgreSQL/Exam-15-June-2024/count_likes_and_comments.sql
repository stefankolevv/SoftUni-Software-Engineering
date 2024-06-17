SELECT p.id AS photo_id,
	   -- DISTINCT == deleting duplicate records.
       COUNT(DISTINCT l.id) AS likes_count,
       COUNT(DISTINCT c.id) AS comments_count
FROM photos p
-- LEFT JOIN == returns all the rows from the left table.
LEFT JOIN likes l ON p.id = l.photo_id
LEFT JOIN comments c ON p.id = c.photo_id
GROUP BY p.id
ORDER BY likes_count DESC, comments_count DESC, p.id ASC;