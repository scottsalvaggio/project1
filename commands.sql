-- CREATE TABLE commands

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    zip_code VARCHAR UNIQUE NOT NULL,
    city VARCHAR NOT NULL,
    state VARCHAR NOT NULL,
    latitude DECIMAL,
    longitude DECIMAL,
    population INTEGER
);

CREATE TABLE check_ins (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    location_id INTEGER REFERENCES locations,
    comment VARCHAR,
    UNIQUE (user_id, location_id)
);

-- Other commands

INSERT INTO users (username, password) VALUES
    ('john', 'j'),
    ('jane', 'jj');

INSERT INTO locations (zip_code, city, state) VALUES
    ('02138', 'Cambridge', 'MA');

INSERT INTO check_ins (user_id, location_id, comment) VALUES
    (1, 1, 'Cambridge 02138 is awesome!'),
    (1, 3, 'Boston 02115 is okay.'),
    (1, 4, 'Cambridge 02139 is almost as great as 02138.');

UPDATE users SET username = 'Jane' WHERE username = 'jane';

SELECT check_ins.id, username, zip_code, city, state, comment
    FROM check_ins JOIN locations ON check_ins.location_id = locations.id
    JOIN users ON check_ins.user_id = users.id;

SELECT users.username, check_ins.comment
    FROM check_ins JOIN locations ON check_ins.location_id = locations.id
    JOIN users ON check_ins.user_id = users.id WHERE locations.id = 7877;

SELECT COUNT(*) FROM check_ins;

SELECT * FROM locations WHERE state='MA' ORDER BY zip_code;

-- Delete *all rows* in table
DELETE FROM <table>;