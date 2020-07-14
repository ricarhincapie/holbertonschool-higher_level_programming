-- Counts and displays occurencies of a data point from a table
SELECT score, COUNT(score) as number from second_table GROUP BY score DESC;
