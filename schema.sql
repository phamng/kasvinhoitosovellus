CREATE TYPE user_type AS ENUM ('user', 'administrator');

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    type user_type
);

CREATE TYPE amount AS ENUM ('Erittäin vähän', 'Vähän', 'Keskimäärin', 'Paljon', 'Erittäin paljon' );

CREATE TABLE plants (
    id SERIAL PRIMARY KEY,
    plant_name TEXT,
    sun amount,
    water amount
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    plant_id INTEGER REFERENCES plants
);