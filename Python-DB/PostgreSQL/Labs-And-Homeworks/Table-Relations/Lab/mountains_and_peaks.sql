CREATE TABLE mountains(
    id serial PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE peaks(
    id serial PRIMARY KEY,
    name VARCHAR(50),
    mountain_id int,
    constraint fk_peaks_mountains
        FOREIGN KEY(mountain_id)
            references mountains(id)
);