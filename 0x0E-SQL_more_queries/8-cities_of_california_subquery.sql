-- Script to create a table with a 
-- Not Null setting.
SELECT id, name FROM cities WHERE state_id =
    (SELECT id FROM states WHERE name = 'California') ORDER BY id;
