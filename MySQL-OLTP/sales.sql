-- Create `sales` database
CREATE DATABASE sales;

use sales;

-- Create `sales_data` table
CREATE TABLE `sales_data` (
	`product_id` INT NOT NULL,
	`customer_id` INT NOT NULL,
	`price` INT NOT NULL,
	`quantity` INT NOT NULL,
	`timestamp` TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP
);

-- Check tables in my database
SHOW TABLES;

SELECT 
    *
FROM
    sales_data;

-- Select count of records in `sales_data` that i have imported from a csv file
SELECT 
    COUNT(*)
FROM
    sales_data;
    

-- Create and index to the timestamp
CREATE INDEX ts ON sales_data (timestamp);


SHOW INDEX FROM sales_data;
    

