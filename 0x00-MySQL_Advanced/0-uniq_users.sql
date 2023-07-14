--  script that creates a table users
-- With these attributes:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)

If the table already exists, your script should not fail
CREATE TABLE IF NOT EXISTS users (
	-- Unique identifier for each user
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	-- Email address of the user
	email VARCHAR(255) NOT NULL UNIQUE,
	-- Name of the user
	name VARCHAR(255)
);
