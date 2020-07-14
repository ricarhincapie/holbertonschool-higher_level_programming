-- Counts and displays occurencies of a data point from a table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score DESC;
