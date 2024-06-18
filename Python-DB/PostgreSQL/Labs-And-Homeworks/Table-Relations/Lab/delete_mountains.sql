CREATE TABLE mountains(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE peaks(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50),
    mountain_id int,
    CONSTRAINT fk_mountain_id FOREIGN KEY(mountain_id)
        references mountains(id)
            ON DELETE CASCADE
);