-- Final Test Query for FinalSQLLexer.g4
-- Includes all special cases required by the project text.

-- 1. Escaped Single Quote inside the String
SELECT 'It''s a beautiful day.' AS Value;
'
'
-- 2. Nested Comments
DECLARE @comment AS VARCHAR(20);
GO
/*
SELECT @comment = '/*';
*/ */
SELECT @@VERSION AS [Version];
GO

-- 3. Splitting a character string (Line Continuation)
SELECT 'abc\
  def' AS [ColumnResult];

-- 4. Splitting a binary string (Line Continuation)
SELECT 0xabc\
def AS [ColumnResult];

-- 5. Comprehensive Test of Keywords, Datatypes, and Literals
CREATE TABLE [dbo].[TestTable] (
    ID BIGINT PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Price MONEY,
    IsActive BIT
);

INSERT INTO [dbo].[TestTable] (ID, Name, Price, IsActive)
VALUES (1, N'Product ''A''', $19.99, 1);

SELECT * FROM [dbo].[TestTable]
WHERE Price BETWEEN 10.00 AND 20.00
AND IsActive = TRUE
ORDER BY Name DESC
OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY;

-- 6. Variables and Identifiers
DECLARE @MyVar INT = 10;
SELECT @MyVar, @@SERVERNAME, [Column With Spaces], "Quoted Identifier";

-- 7. Hex and Bit Literals
SELECT 0xDEADBEEF AS HexValue, 0 AS BitValue;
