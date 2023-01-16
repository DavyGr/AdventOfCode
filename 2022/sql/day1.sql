-- SQL Server
USE mydb;


-- Temp table with input values
DROP TABLE IF EXISTS 	day01_input;
CREATE TABLE		day01_input (
	value 		int
);

-- Table with input values AND id column
DROP TABLE IF EXISTS 	day01;
CREATE TABLE 		day01 (
	id		int IDENTITY(1,1) PRIMARY KEY -- creates an auto-increment id-column
	, value		int
);

-- Insert the input values into the temp input table
BULK INSERT 	day01_input
		-- USE FULL PATH BELOW!
FROM 		'2022\inputs\01.txt'
WITH
(
		ROWTERMINATOR ='\n'
);

--  Insert the input values into the table WITH id column
INSERT INTO 	day01 (value)
SELECT 		value 
FROM 		day01_input;


-- Assign a groupId to the values and sum the values per groupId

/* The groupId assignment works as follows:
 * In the input dataset, all rows have a row_number id. Including NULL-rows. ('old_id')
 * In the query below, we use the same dataset but filter out NULL-rows in the WHERE-clause. Then we assign a new row_number id. ('new_id')
 * Thus, for every NULL-row, an offset of +1 is created between old_id and new_id.
 * When we subtract new_id from old_id, an incrementing groupId is created.
 */
DROP TABLE IF EXISTS 	day01_grouped;
WITH a 	AS 
( 	SELECT	--id
		--, ROW_NUMBER() OVER(ORDER BY id) AS rn
		id - ROW_NUMBER() OVER(ORDER BY id) AS groupId
		, value
	FROM 	day01
	WHERE 	value IS NOT NULL
)
SELECT		a.groupId
		, sum(a.value) AS sum_value
INTO 	 	day01_grouped
FROM 	 	a
GROUP BY 	a.groupId;


-- Find highest sum_value
SELECT 	 TOP(1) sum_value
FROM 	 day01_grouped 
ORDER BY sum_value DESC;

-- Find SUM of the 3 highest sum_values
WITH a 	AS
(	SELECT 		TOP(3) sum_value
	FROM 		day01_grouped
	ORDER BY	sum_value DESC
)
SELECT 	sum(a.sum_value) AS sum_top_3
FROM 	a;
