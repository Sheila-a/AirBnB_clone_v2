-- this script creates a database base and
-- also create a user for the AirBnB clone project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON `performance_schema`.* TO `hbnb_dev`@`localhost`;
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO `hbnb_dev`@`localhost`;
