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
    user_id INTEGER REFERENCES users NOT NULL,
    location_id INTEGER REFERENCES locations NOT NULL,
    comment VARCHAR,
    UNIQUE (user_id, location_id)
);