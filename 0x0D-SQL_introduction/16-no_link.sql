-- Get average score from a table
SELECT score, name from second_table HAVING name IS NOT NULL ORDER BY score DESC;
