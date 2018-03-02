-- Creates a new schema/database
CREATE SCHEMA application;
USE application;

-- Creates a table in the schema
CREATE TABLE `users` (
    `id` INT(20) NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(30) NOT NULL,    
    `last_name` VARCHAR(30) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `messages` (
    `id` INT(20) NOT NULL AUTO_INCREMENT,
    `message` VARCHAR(255) NOT NULL,
    `recipient_user_id` INT(20) NOT NULL,
    `sender_user_id` INT(20) NOT NULL,
    PRIMARY KEY(`id`)
);

DROP TABLE `users`;

SELECT * FROM `users`;
SELECT * FROM `messages`;

INSERT INTO `users`(first_name, last_name)
VALUES ('User', 'One'),
('User', 'Two')
;


SELECT * -- fields to select
FROM users
WHERE first_name = 'User'
AND last_name = 'One'
;

SELECT first_name, last_name
FROM names
WHERE email = 'cdunning@gmail.com';


SELECT `id` FROM `users` WHERE first_name = 'User' AND last_name = 'One';

INSERT INTO `messages` (message, recipient_user_id, sender_user_id) VALUES ('Test message body', 1, 2);



SELECT `id` FROM `messages` LIMIT 1;

INSERT INTO users (first_name, last_name) VALUES ("User", "One");
INSERT INTO users (first_name, last_name) VALUES ("User", "Two");
INSERT INTO users (first_name, last_name) VALUES ("User", "Three");



