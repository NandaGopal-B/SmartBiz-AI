CREATE DATABASE IF NOT EXISTS smartbiz;
USE smartbiz;

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(20),
    city VARCHAR(80),
    annual_income DECIMAL(12,2),
    total_spend DECIMAL(12,2),
    purchase_frequency INT,
    recency_days INT,
    churned BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    category VARCHAR(80),
    price DECIMAL(12,2),
    stock INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    amount DECIMAL(12,2),
    region VARCHAR(80),
    sale_month INT
);
