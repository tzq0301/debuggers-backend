DROP DATABASE IF EXISTS debuggers;
CREATE DATABASE IF NOT EXISTS debuggers;
USE debuggers;

DROP TABLE IF EXISTS user;
CREATE TABLE IF NOT EXISTS user
(
    `username` VARCHAR(50) PRIMARY KEY,
    `password` VARCHAR(50) NOT NULL
);

CREATE INDEX idx_username_password ON user(`username`, `password`);