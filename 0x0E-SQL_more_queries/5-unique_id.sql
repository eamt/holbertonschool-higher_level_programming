-- Creates the table `unique_id`
-- In MySQL Server with a UNIQUE colunxsz
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL
);
