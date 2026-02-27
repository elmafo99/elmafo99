CREATE TABLE IF NOT EXISTS employees (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    birth_date VARCHAR(100),
    first_name VARCHAR(100) NOT NULL, 
    last_name VARCHAR (100) NOT NULL


)

ALTER TABLE employees ALTER COLUMN birth_date TYPE DATE USING birth_date::date;

ALTER TABLE employees ADD COLUMN salary NUMERIC(10,2);
ALTER TABLE employees ADD COLUMN title VARCHAR(100);
ALTER TABLE employees ADD COLUMN title_date DATE;

SELECT * FROM employees;

INSERT INTO employees (birth_date, first_name, last_name, salary, title, title_date)
VALUES('1990-05-15', 'Ana', 'García', 45000, 'Senior Designer', '2020-01-10'),
('1985-08-22', 'Ana', 'Martínez', 32000, 'Product Manager', '2019-03-15'),
('1992-11-30', 'Ana', 'López', 28000, 'Fashion Stylist', '2020-06-12'),
('1988-02-10', 'Carlos', 'Ruiz', 50000, 'Creative Director', '2018-11-20'),
('1995-07-04', 'Carlos', 'Sánchez', 12000, 'Junior Tailor', '2020-02-25'),
('1991-03-19', 'Laura', 'Pérez', 38000, 'Marketing Lead', '2020-09-01'),
('1987-12-05', 'Javier', 'Gómez', 25000, 'Photographer', '2021-04-10'),
('1993-01-25', 'Marta', 'Díaz', 15000, 'Sales Assistant', '2020-05-20'),
('1989-09-14', 'Diego', 'Torres', 42000, 'Supply Chain Specialist', '2017-08-30'),
('1994-06-30', 'Elena', 'Vázquez', 8500, 'Showroom Assistant', '2022-01-15'),
('1986-04-12', 'Sergio', 'Castro', 31000, 'Pattern Maker', '2019-12-05'),
('1990-10-22', 'Lucía', 'Blanco', 19000, 'Social Media Manager', '2021-07-22'),
('1992-05-08', 'Ricardo', 'Molina', 5500, 'Intern', '2023-03-10'),
('1984-11-17', 'Isabel', 'Ortiz', 48000, 'E-commerce Manager', '2016-02-28'),
('1996-02-29', 'Hugo', 'Serrano', 22000, 'Warehouse Operator', '2022-11-11');


SELECT * FROM employees;

SELECT first_name, salary FROM employees;

SELECT * FROM employees WHERE id=2;
SELECT * FROM employees WHERE salary>20000; 
SELECT * FROM employees WHERE salary<=10000;

UPDATE employees SET first_name='Pepe' WHERE id=7;
DELETE FROM employees WHERE id=5;
DELETE FROM employees WHERE id>20000;
SELECT * FROM employees WHERE salary BETWEEN 14000 AND 50000;

SELECT * FROM employees ORDER BY birth_date DESC;

SELECT DISTINCT first_name FROM employees;
SELECT first_name ||' '|| last_name AS complete_name FROM employees WHERE id=9;
SELECT * FROM employees WHERE first_name LIKE 'P%';
SELECT * FROM employees WHERE first_name LIKE '%a%';

SELECT COUNT(id) FROM employees; --contar el número de empleados en la tabla
SELECT first_name, last_name, salary FROM employees WHERE salary=(SELECT MAX(salary) FROM employees);

SELECT title, ROUND(AVG(salary),2) FROM employees GROUP BY title; --se pone el round para redondear a 2 decimales
SELECT title, MAX(salary) FROM employees GROUP BY title;
SELECT title, MIN(salary) FROM employees GROUP BY title;

SELECT first_name, ROUND((salary), 2) AS salario_redondeado FROM employees; -- ponemos el AS para cambiar el nombre de la columna

SELECT salary, ROUND((salary*0.21),2) AS impuestos, ROUND((salary-(salary*0.21)),2) AS salario_neto FROM employees;
SELECT first_name, salary FROM employees;




CREATE TABLE IF NOT EXISTS departments(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100)

)

INSERT INTO departments(name) VALUES('Engineering'), ('Marketing');

SELECT * FROM departments;

ALTER TABLE employees ADD COLUMN departments_id BIGINT;
SELECT * FROM employees INNER JOIN departments ON departments.id = employees.departments_id;

UPDATE employees SET departments_id = 1 WHERE id=1;
UPDATE employees SET departments_id=1 WHERE id=2;
UPDATE EMPLOYEES SET departments_id=2 WHERE id=3;

SELECT * FROM EMPLOYEES;

SELECT employees.first_name, employees.last_name, departments.name AS department FROM employees;
INNER JOIN departments ON departments.id = employees.departments_id;