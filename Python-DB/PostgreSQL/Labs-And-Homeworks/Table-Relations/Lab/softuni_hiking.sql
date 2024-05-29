SELECT
    r.start_point,
    r.end_point,
    r.leader_id,
    CONCAT(c.first_name, ' ', c.last_name) AS leader_name
FROM campers AS c
    JOIN routes AS r
        ON c.id = r.leader_id