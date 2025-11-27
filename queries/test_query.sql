-- Sample SQL Query to test CombinedSQLLexer.g4
-- Testing keywords, datatypes, literals, identifiers, and comments

-- 1. Keywords and Datatypes
CREATE TABLE [dbo].[Employees] (
    EmployeeID INT_TYPE PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NULL,
    HireDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Salary DECIMAL_TYPE(10, 2),
    IsActive BIT
);

-- 2. SELECT statement with various clauses
SELECT
    e.EmployeeID,
    e.FirstName,
    e.LastName,
    e.Salary * 1.10 AS NewSalary,
    'Active' AS Status
FROM
    [dbo].[Employees] AS e
WHERE
    e.IsActive = TRUE
    AND e.Salary BETWEEN 50000.00 AND 100000.00
    OR e.LastName LIKE N'Smi%' -- Unicode string literal
ORDER BY
    NewSalary DESC
OFFSET 10 ROWS FETCH NEXT 5 ROWS ONLY;

-- 3. INSERT statement with literals and variables
INSERT INTO [dbo].[Employees] (EmployeeID, FirstName, LastName, Salary, IsActive)
VALUES
    (101, 'John', 'Doe', 65000.00, 1),
    (102, 'Jane', 'Smith', 95000.00, 0);

DECLARE @MaxSalary MONEY;
SET @MaxSalary = $100000.00; -- Money literal

-- 4. Nested Block Comment
/*
This is a block comment.
It can contain nested comments: /* Nested Comment */
And it should be skipped by the lexer.
*/

-- 5. Identifier types
SELECT
    [EmployeeID], -- Bracketed identifier
    "FirstName", -- Double-quoted identifier
    @MaxSalary, -- User variable
    @@VERSION -- System variable
FROM
    [dbo].[Employees];

-- 6. Operators
SELECT 1 + 2 * 3 / 4 % 5;
UPDATE [dbo].[Employees] SET Salary += 1000.00 WHERE EmployeeID = 101;



-- Test 1: Basic SELECT with data types
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2),
    hire_date DATE,
    is_active BIT,
    profile_data XML
);

-- Test 2: String literals (both types)
SELECT 'Hello World' AS greeting, 
       N'Unicode String' AS unicode_text,
       0x48656C6C6F AS hex_value;

-- Test 3: All numeric types
INSERT INTO test_numbers VALUES (
    123,                    -- INT
    123.456,               -- DECIMAL
    1.23E+10,              -- FLOAT with exponent
    $100.50,               -- MONEY
    0b1010,                -- BIT
    0x1A2B                 -- HEX
);

-- Test 4: Reserved keywords
SELECT * FROM users 
WHERE age BETWEEN 18 AND 65
AND status IN ('active', 'pending')
ORDER BY created_date DESC;

-- Test 5: Complex query with JOINs
SELECT e.name, d.department_name, e.salary
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id
LEFT OUTER JOIN salaries s ON e.id = s.emp_id
WHERE e.hire_date > '2020-01-01'
GROUP BY d.department_name
HAVING AVG(e.salary) > 50000;

-- Test 6: Operators
SELECT a + b, a - b, a * b, a / b, a % b,
       a = b, a != b, a <> b, a < b, a <= b, a > b, a >= b,
       a & b, a | b, a ^ b,
       NOT active, a IS NULL, b IS NOT NULL;

-- Test 7: Functions and CASE
SELECT 
    CASE 
        WHEN salary > 100000 THEN 'High'
        WHEN salary > 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_bracket,
    COALESCE(bonus, 0) AS actual_bonus,
    CONVERT(VARCHAR(10), hire_date, 101) AS formatted_date;

-- Test 8: Subqueries
SELECT * FROM (
    SELECT name, salary, 
           ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
    FROM employees
) ranked_employees
WHERE rank <= 10;

-- Test 9: Variables and identifiers
DECLARE @count INT = 0;
DECLARE @@version VARCHAR(100);
SELECT @user_name = name FROM users WHERE id = [User ID];
SELECT name FROM [My Table With Spaces];
SELECT @@SERVERNAME, @local_variable;

-- Test 10: Comments
-- This is a single line comment
/* This is a 
   multi-line comment */
SELECT * FROM table /* inline comment */ WHERE id = 1;

-- Test 11: Transactions
BEGIN TRANSACTION;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Test 12: Missing keywords test
CHECKPOINT;  -- Should work in SQLLexer2? NO - it's missing!
BROWSE table_name;  -- Should work in TSQLLexer? YES

-- Test 13: Data type declarations
DECLARE @name NVARCHAR(MAX);
DECLARE @id BIGINT;
DECLARE @price SMALLMONEY;
DECLARE @data VARBINARY(MAX);
DECLARE @created DATETIME2(7);

-- Test 14: Edge cases
SELECT '', NULL, 0, 0.0, -1, +1;
SELECT 'O''Reilly' AS company;  -- Escaped quote
-- SELECT N'日本語' AS japanese;  -- Unicode