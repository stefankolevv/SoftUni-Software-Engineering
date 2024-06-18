SELECT
    replace(title, 'The', '***')
FROM books
WHERE left(title, 3) = 'The'