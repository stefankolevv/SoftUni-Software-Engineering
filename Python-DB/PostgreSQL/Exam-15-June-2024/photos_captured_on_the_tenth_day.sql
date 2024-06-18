CREATE OR REPLACE FUNCTION fn_photos_captured_on_tenth_day()
RETURNS TABLE (
    summary VARCHAR(13),
    date VARCHAR(12)
) AS
$$
BEGIN
    RETURN QUERY
    SELECT 
        -- Truncate if description > 10 chars.
        CASE 
            WHEN LENGTH(description) > 10 THEN SUBSTRING(description FROM 1 FOR 10) || '...' 
            ELSE description 
        END::VARCHAR(13) AS summary,
        -- Format: 'DD.MM HH24:MI' (as required).
        TO_CHAR(capture_date, 'DD.MM HH24:MI')::VARCHAR(12) AS date
    FROM photos
    WHERE EXTRACT(DAY FROM capture_date) = 10
    ORDER BY capture_date DESC;
END;
$$
LANGUAGE plpgsql;