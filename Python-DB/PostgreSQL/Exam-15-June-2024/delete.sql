DELETE FROM addresses
-- divide by 2 + street name contains the letter 'r'.
WHERE id % 2 = 0 AND street ILIKE '%r%';