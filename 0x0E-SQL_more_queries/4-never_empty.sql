-- Script to create a table with a 
-- Default setting.
DROP TABLE IF EXISTS id_not_null;
CREATE TABLE id_not_null (
    id INT DEFAULT '1', 
    name VARCHAR(256)
);
