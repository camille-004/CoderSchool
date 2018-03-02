-- Creates a new schema/database
CREATE SCHEMA coder_school;
USE coder_school;

-- Creates a table in the schema
CREATE TABLE `names` (
	`email` VARCHAR(35),
    `first_name` VARCHAR(30),
    `last_name` VARCHAR(30)
);

SELECT * FROM `names`;

INSERT INTO `names`(email, first_name, last_name)
-- VALUES ('cdunning@gmail.com', 'Camille', 'Dunning');
VALUES ('userone@gmail.com', 'User', 'One'),
('usertwo@gmail.com', 'User', 'Two'),
('userthree@gmail.com', 'User', 'Three'),
('userfour@gmail.com', 'User', 'Four');


SELECT * -- fields to select
FROM names
WHERE first_name = 'User'
AND last_name = 'One'
;

SELECT first_name, last_name
FROM names
WHERE email = 'cdunning@gmail.com';