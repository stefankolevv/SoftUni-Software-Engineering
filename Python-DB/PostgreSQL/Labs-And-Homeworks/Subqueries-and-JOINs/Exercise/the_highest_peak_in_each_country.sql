-- 6 # USPESHEN
WITH row_number AS (
  SELECT
    c.country_name,                           
    p.peak_name AS highest_peak_name,         
    p.elevation AS highest_peak_elevation,    
    m.mountain_range,                         
    ROW_NUMBER() OVER (
      PARTITION BY c.country_name             
      ORDER BY p.elevation DESC               
    ) AS peak_rank
  FROM
    countries c
    LEFT JOIN mountains_countries mc ON c.country_code = mc.country_code  
    LEFT JOIN peaks p ON mc.mountain_id = p.mountain_id                  
    LEFT JOIN mountains m ON p.mountain_id = m.id                        
)

SELECT
  country_name,
  COALESCE(highest_peak_name, '(no highest peak)') AS highest_peak_name,          
  COALESCE(highest_peak_elevation, 0) AS highest_peak_elevation,                  
  COALESCE(mountain_range, '(no mountain)') AS mountain                           
FROM
  row_number
WHERE
  peak_rank = 1                      
ORDER BY
  country_name ASC,                  
  highest_peak_elevation DESC;       