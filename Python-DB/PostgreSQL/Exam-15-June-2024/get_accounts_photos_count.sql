CREATE OR REPLACE FUNCTION udf_accounts_photos_count(
	account_username VARCHAR(30)
) RETURNS INT 
AS 
$$
DECLARE -- DECLARE == initializes a Transact-SQL variable
    photo_count INT;
BEGIN
    SELECT COUNT(*) -- Calculating the number of rows in the table.
    INTO photo_count
    FROM accounts_photos ap
    JOIN accounts a ON ap.account_id = a.id
    WHERE a.username = account_username;

    RETURN photo_count;
END;
$$ 
LANGUAGE plpgsql;