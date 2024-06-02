UPDATE countries
SET country_name = 'Burma'
WHERE country_name = 'Myanmar';

INSERT INTO monasteries (monastery_name, country_code)
VALUES ('Hanga Abbey', 'TZ');

INSERT INTO monasteries (monastery_name, country_code)
VALUES ('Myin-Tin-Daik', 'MM');

WITH monasteries_count AS (
    SELECT
        co.continent_name,
        c.country_name,
        COUNT(m.id) AS monastery_count
    FROM
        continents AS co
        LEFT JOIN countries c ON co.continent_code = c.continent_code
        LEFT JOIN monasteries m ON c.country_code = m.country_code
    WHERE
        NOT c.three_rivers OR c.three_rivers IS NULL
    GROUP BY
        c.country_name, co.continent_name
)
SELECT
    continent_name,
    country_name,
    monastery_count
FROM
    monasteries_count
ORDER BY
    monastery_count DESC,
    country_name ASC;
