-- Script to create a table with a 
-- Not Null setting.
DROP TABLE IF EXISTS force_name;
CREATE TABLE force_name (
    id INT, 
    name VARCHAR(256) NOT NULL
);
