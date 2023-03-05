CREATE TYPE user_type AS ENUM ('user', 'administrator');
CREATE TYPE amount AS ENUM ('Erittäin vähän', 'Vähän', 'Keskimäärin', 'Paljon', 'Erittäin paljon' );

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT,
    type user_type
);

CREATE TABLE plants (
    id SERIAL PRIMARY KEY,
    plant_name TEXT NOT NULL UNIQUE,
    sun amount,
    water amount
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    plant_id INTEGER REFERENCES plants
);

CREATE TABLE likes (
    PRIMARY KEY (user_id, plant_id),
    user_id INTEGER REFERENCES users,
    plant_id INTEGER REFERENCES plants
);

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE group_values (
    PRIMARY KEY (group_id, plant_id),
    group_id INTEGER REFERENCES groups,
    plant_id INTEGER REFERENCES plants
);