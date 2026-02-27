CREATE TABLE IF NOT EXISTS users (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR (255) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    register_date TIMESTAMPTZ NOT NULL DEFAULT now()


)

TRUNCATE TABLE users;

DROP TABLE users;

SELECT * FROM users;

ALTER TABLE users ADD COLUMN age VARCHAR(3);

SELECT * FROM users;

ALTER TABLE users ALTER COLUMN age TYPE INTEGER USING age::integer;

ALTER TABLE users DROP COLUMN age;

SELECT * FROM users;



INSERT INTO users (first_name, last_name, email, password, age)
VALUES ('Ada', 'Lovelace', 'adalovelace@gmail.com', 12345, 36);

SELECT * FROM users;

