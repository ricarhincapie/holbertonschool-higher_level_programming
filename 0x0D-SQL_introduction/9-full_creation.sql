-- Creates a second_table and inserts some data in it
DROP TABLE IF EXISTS second_table;
CREATE TABLE second_table (
    id INT,
    name VARCHAR(256),
    score INT);
INSERT INTO second_table (
    id, name, score
)
VALUES
    (
        1, 'Jhon', 10
    ),
    (
        2, 'Alex', 3
    ),
    (
        3, 'Bob', 14
    ),
    (
        4, 'George', 8
    );
