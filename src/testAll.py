"""
Automated test suite for SQL Lexer using ANTLR4
Requirements: pip install antlr4-python3-runtime
"""

from antlr4 import *
from io import StringIO
import sys

# Import your generated lexer
# You'll need to generate the Python lexer first using:
# antlr4 -Dlanguage=Python3 SQLLexer.g4
try:
    from generated.SQLLexer import SQLLexer
except ImportError:
    print("Error: Please generate the Python lexer first using:")
    print("antlr4 -Dlanguage=Python3 SQLLexer.g4")
    sys.exit(1)

# Test cases: (query, expected_tokens)
TEST_CASES = [
    {
        "name": "Test 1: Simple SELECT",
        "query": "SELECT * FROM users WHERE id = 123;",
        "expected": [
            "SELECT",
            "STAR",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "WHERE",
            "UNQUOTED_IDENTIFIER",
            "EQ",
            "NUMBER_LITERAL",
            "SEMI",
        ],
    },
    {
        "name": "Test 2: String Literals",
        "query": "SELECT 'Hello World', N'Unicode String';",
        "expected": [
            "SELECT",
            "STRING_LITERAL",
            "COMMA",
            "UNICODE_STRING_LITERAL",
            "SEMI",
        ],
    },
    {
        "name": "Test 3: Bracket Identifiers",
        "query": "SELECT [User Name], [Order Date] FROM [Sales Data];",
        "expected": [
            "SELECT",
            "BRACKET_IDENTIFIER",
            "COMMA",
            "BRACKET_IDENTIFIER",
            "FROM",
            "BRACKET_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test 4: Variables",
        "query": "SELECT @user_id, @@VERSION;",
        "expected": ["SELECT", "USER_VARIABLE", "COMMA", "SYSTEM_VARIABLE", "SEMI"],
    },
    {
        "name": "Test 5: Operators and Numbers",
        "query": "UPDATE table1 SET value += 10.5 WHERE amount >= 100;",
        "expected": [
            "UPDATE",
            "UNQUOTED_IDENTIFIER",
            "SET",
            "UNQUOTED_IDENTIFIER",
            "PLUS_EQ",
            "NUMBER_LITERAL",
            "WHERE",
            "UNQUOTED_IDENTIFIER",
            "GTE",
            "NUMBER_LITERAL",
            "SEMI",
        ],
    },
    {
        "name": "Test 6: Comments",
        "query": "-- This is a line comment\nSELECT col1 /* block comment */ FROM table1;",
        "expected": [
            "SELECT",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test 7: Hex Literal",
        "query": "SELECT 0xFF, 0x1A2B;",
        "expected": ["SELECT", "HEX_LITERAL", "COMMA", "HEX_LITERAL", "SEMI"],
    },
    {
        "name": "Test 8: CASE Statement",
        "query": "SELECT CASE WHEN age > 18 THEN 'Adult' ELSE 'Minor' END;",
        "expected": [
            "SELECT",
            "CASE",
            "WHEN",
            "UNQUOTED_IDENTIFIER",
            "GT",
            "NUMBER_LITERAL",
            "THEN",
            "STRING_LITERAL",
            "ELSE",
            "STRING_LITERAL",
            "END",
            "SEMI",
        ],
    },
    {
        "name": "Test 9: JOIN with Aliases",
        "query": "SELECT u.name, o.total FROM users AS u INNER JOIN orders o ON u.id = o.user_id;",
        "expected": [
            "SELECT",
            "UNQUOTED_IDENTIFIER",
            "DOT",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "DOT",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "AS",
            "UNQUOTED_IDENTIFIER",
            "INNER",
            "JOIN",
            "UNQUOTED_IDENTIFIER",
            "UNQUOTED_IDENTIFIER",
            "ON",
            "UNQUOTED_IDENTIFIER",
            "DOT",
            "UNQUOTED_IDENTIFIER",
            "EQ",
            "UNQUOTED_IDENTIFIER",
            "DOT",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test 10: Data Types",
        "query": "CREATE TABLE test (id INT, name VARCHAR(50), created DATETIME);",
        "expected": [
            "CREATE",
            "TABLE",
            "UNQUOTED_IDENTIFIER",
            "LPAREN",
            "UNQUOTED_IDENTIFIER",
            "INT_TYPE",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "VARCHAR",
            "LPAREN",
            "NUMBER_LITERAL",
            "RPAREN",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "DATETIME",
            "RPAREN",
            "SEMI",
        ],
    },
    {
        "name": "Test 11: Boolean and NULL literals",
        "query": "SELECT TRUE, FALSE, NULL FROM flags;",
        "expected": [
            "SELECT",
            "TRUE",
            "COMMA",
            "FALSE",
            "COMMA",
            "NULL",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test 12: Bit and money literals",
        "query": "SELECT B'1010', B'0', $123.45, B'111111';",
        "expected": [
            "SELECT",
            "BIT_LITERAL",
            "COMMA",
            "BIT_LITERAL",
            "COMMA",
            "MONEY_LITERAL",
            "COMMA",
            "BIT_LITERAL",
            "SEMI",
        ],
    },
    {
        "name": "Test 13: Mixed numeric formats",
        "query": "SELECT 10, 3.14, .5, 1e10, 2.5E-3 FROM nums;",
        "expected": [
            "SELECT",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test 14: Money and hex literals",
        "query": "SELECT $1.00, 0x1A, 0xFFEE FROM t1;",
        "expected": [
            "SELECT",
            "MONEY_LITERAL",
            "COMMA",
            "HEX_LITERAL",
            "COMMA",
            "HEX_LITERAL",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test 15: Different identifier styles",
        "query": 'SELECT col_1, "Col 2", [Col 3] FROM #tmp_table;',
        "expected": [
            "SELECT",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "DOUBLE_QUOTED_IDENTIFIER",
            "COMMA",
            "BRACKET_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test 16: User and system variables",
        "query": "SELECT @var1, @@VERSION, @user_name FROM config;",
        "expected": [
            "SELECT",
            "USER_VARIABLE",
            "COMMA",
            "SYSTEM_VARIABLE",
            "COMMA",
            "USER_VARIABLE",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test 17: All assignment operators",
        "query": "UPDATE t SET a = 1, b += 2, c -= 3, d *= 4, e /= 5, f %= 6;",
        "expected": [
            "UPDATE",
            "UNQUOTED_IDENTIFIER",
            "SET",
            "UNQUOTED_IDENTIFIER",
            "EQ",
            "NUMBER_LITERAL",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "PLUS_EQ",
            "NUMBER_LITERAL",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "MINUS_EQ",
            "NUMBER_LITERAL",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "STAR_EQ",
            "NUMBER_LITERAL",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "SLASH_EQ",
            "NUMBER_LITERAL",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "PERCENT_EQ",
            "NUMBER_LITERAL",
            "SEMI",
        ],
    },
    {
        "name": "Test 18: Comparison operators",
        "query": "SELECT * FROM t WHERE a = 1 AND b != 2 AND c <> 3 AND d <= 4 AND e >= 5 AND f < 6 AND g > 7;",
        "expected": [
            "SELECT",
            "STAR",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "WHERE",
            "UNQUOTED_IDENTIFIER",
            "EQ",
            "NUMBER_LITERAL",
            "AND",
            "UNQUOTED_IDENTIFIER",
            "NEQ",
            "NUMBER_LITERAL",
            "AND",
            "UNQUOTED_IDENTIFIER",
            "NEQ",
            "NUMBER_LITERAL",
            "AND",
            "UNQUOTED_IDENTIFIER",
            "LTE",
            "NUMBER_LITERAL",
            "AND",
            "UNQUOTED_IDENTIFIER",
            "GTE",
            "NUMBER_LITERAL",
            "AND",
            "UNQUOTED_IDENTIFIER",
            "LT",
            "NUMBER_LITERAL",
            "AND",
            "UNQUOTED_IDENTIFIER",
            "GT",
            "NUMBER_LITERAL",
            "SEMI",
        ],
    },
    {
        "name": "Test 19: Bitwise operators",
        "query": "SELECT a & b, c | d, e ^ f FROM t;",
        "expected": [
            "SELECT",
            "UNQUOTED_IDENTIFIER",
            "AMPERSAND",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "PIPE",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "CARET",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test 20: Nested block comments",
        "query": "SELECT 1 /* outer /* nested */ still comment */ FROM t;",
        "expected": [
            "SELECT",
            "NUMBER_LITERAL",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test 21: Data type keywords",
        "query": "CREATE TABLE t (id BIGINT, price MONEY, flag BIT, created DATE, updated DATETIME, payload XML);",
        "expected": [
            "CREATE",
            "TABLE",
            "UNQUOTED_IDENTIFIER",
            "LPAREN",
            "UNQUOTED_IDENTIFIER",
            "BIGINT",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "MONEY",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "BIT",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "DATE",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "DATETIME",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "XML",
            "RPAREN",
            "SEMI",
        ],
    },
    {
        "name": "Test 22: Function and date/time keywords",
        "query": "SELECT CURRENT_DATE, CURRENT_TIME, CURRENT_TIMESTAMP, CURRENT_USER, SESSION_USER, SYSTEM_USER;",
        "expected": [
            "SELECT",
            "CURRENT_DATE",
            "COMMA",
            "CURRENT_TIME",
            "COMMA",
            "CURRENT_TIMESTAMP",
            "COMMA",
            "CURRENT_USER",
            "COMMA",
            "SESSION_USER",
            "COMMA",
            "SYSTEM_USER",
            "SEMI",
        ],
    },
    {
        "name": "Test 23: JOIN with keywords and aliases",
        "query": "SELECT t.id, t2.name FROM t INNER JOIN t2 ON t.id = t2.id WHERE t.id BETWEEN 1 AND 10;",
        "expected": [
            "SELECT",
            "UNQUOTED_IDENTIFIER",
            "DOT",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "DOT",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "INNER",
            "JOIN",
            "UNQUOTED_IDENTIFIER",
            "ON",
            "UNQUOTED_IDENTIFIER",
            "DOT",
            "UNQUOTED_IDENTIFIER",
            "EQ",
            "UNQUOTED_IDENTIFIER",
            "DOT",
            "UNQUOTED_IDENTIFIER",
            "WHERE",
            "UNQUOTED_IDENTIFIER",
            "BETWEEN",
            "NUMBER_LITERAL",
            "AND",
            "NUMBER_LITERAL",
            "SEMI",
        ],
    },
    {
        "name": "Test 24: ORDER BY and TOP",
        "query": "SELECT TOP 10 id, name FROM t ORDER BY name DESC;",
        "expected": [
            "SELECT",
            "TOP",
            "NUMBER_LITERAL",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "ORDER",
            "BY",
            "UNQUOTED_IDENTIFIER",
            "DESC",
            "SEMI",
        ],
    },
    {
        "name": "Test A1: Many keywords in one statement",
        "query": """
            BEGIN TRANSACTION;
            CREATE TABLE dbo.T1 (
                id INT PRIMARY KEY,
                amount DECIMAL,
                created DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            INSERT INTO dbo.T1 (id, amount, created)
            VALUES (1, 10.5, CURRENT_TIMESTAMP);
            COMMIT TRANSACTION;
        """,
        "expected": [
            "BEGIN",
            "TRANSACTION",
            "SEMI",
            "CREATE",
            "TABLE",
            "UNQUOTED_IDENTIFIER",
            "LPAREN",
            "UNQUOTED_IDENTIFIER",
            "INT_TYPE",
            "PRIMARY",
            "KEY",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "DECIMAL_TYPE",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "DATETIME",
            "DEFAULT",
            "CURRENT_TIMESTAMP",
            "RPAREN",
            "SEMI",
            "INSERT",
            "INTO",
            "UNQUOTED_IDENTIFIER",
            "LPAREN",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "RPAREN",
            "VALUES",
            "LPAREN",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "COMMA",
            "CURRENT_TIMESTAMP",
            "RPAREN",
            "SEMI",
            "COMMIT",
            "TRANSACTION",
            "SEMI",
        ],
    },
    {
        "name": "Test A2: All numeric literal forms",
        "query": "SELECT 0, 123, 123., .123, 1.23E10, 4e-3, .5E+2 FROM t;",
        "expected": [
            "SELECT",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test A3: Money literals with different currency symbols",
        "query": "SELECT $1.00, ¢2.50, £3.75, ¥100.00 FROM prices;",
        "expected": [
            "SELECT",
            "MONEY_LITERAL",
            "COMMA",
            "MONEY_LITERAL",
            "COMMA",
            "MONEY_LITERAL",
            "COMMA",
            "MONEY_LITERAL",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test A5: Bit literals and booleans",
        "query": "SELECT B'0', B'1', B'101010', TRUE, FALSE FROM flags;",
        "expected": [
            "SELECT",
            "BIT_LITERAL",
            "COMMA",
            "BIT_LITERAL",
            "COMMA",
            "BIT_LITERAL",
            "COMMA",
            "TRUE",
            "COMMA",
            "FALSE",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test A6: String literals with escapes and newlines",
        "query": "SELECT 'single ''quote''', N'unicode ''ط''', 'line1\\\nline2' FROM t;",
        "expected": [
            "SELECT",
            "STRING_LITERAL",
            "COMMA",
            "UNICODE_STRING_LITERAL",
            "COMMA",
            "STRING_LITERAL",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test A7: Identifiers – unquoted, bracketed, double-quoted",
        "query": 'SELECT col1, [Complex Name], "Another Name", #temp, _x1, a@b FROM dbo.[My Table];',
        "expected": [
            "SELECT",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "BRACKET_IDENTIFIER",
            "COMMA",
            "DOUBLE_QUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "DOT",
            "BRACKET_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test A8: User and system variables edge cases",
        "query": "SELECT @v, @Var_1, @@VERSION, @@sysVar42 FROM t;",
        "expected": [
            "SELECT",
            "USER_VARIABLE",
            "COMMA",
            "USER_VARIABLE",
            "COMMA",
            "SYSTEM_VARIABLE",
            "COMMA",
            "SYSTEM_VARIABLE",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test A9: All arithmetic and assignment operators",
        "query": "UPDATE t SET a=1+2-3*4/5%6, b+=1, c-=2, d*=3, e/=4, f%=5;",
        "expected": [
            "UPDATE",
            "UNQUOTED_IDENTIFIER",
            "SET",
            "UNQUOTED_IDENTIFIER",
            "EQ",
            "NUMBER_LITERAL",
            "PLUS",
            "NUMBER_LITERAL",
            "MINUS",
            "NUMBER_LITERAL",
            "STAR",
            "NUMBER_LITERAL",
            "SLASH",
            "NUMBER_LITERAL",
            "PERCENT_OP",
            "NUMBER_LITERAL",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "PLUS_EQ",
            "NUMBER_LITERAL",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "MINUS_EQ",
            "NUMBER_LITERAL",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "STAR_EQ",
            "NUMBER_LITERAL",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "SLASH_EQ",
            "NUMBER_LITERAL",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "PERCENT_EQ",
            "NUMBER_LITERAL",
            "SEMI",
        ],
    },
    {
        "name": "Test A10: Comparison and logical operators",
        "query": "SELECT * FROM t WHERE a = 1 AND b != 2 OR c <> 3 AND d <= 4 OR e >= 5 AND f < 6 OR g > 7;",
        "expected": [
            "SELECT",
            "STAR",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "WHERE",
            "UNQUOTED_IDENTIFIER",
            "EQ",
            "NUMBER_LITERAL",
            "AND",
            "UNQUOTED_IDENTIFIER",
            "NEQ",
            "NUMBER_LITERAL",
            "OR",
            "UNQUOTED_IDENTIFIER",
            "NEQ",
            "NUMBER_LITERAL",
            "AND",
            "UNQUOTED_IDENTIFIER",
            "LTE",
            "NUMBER_LITERAL",
            "OR",
            "UNQUOTED_IDENTIFIER",
            "GTE",
            "NUMBER_LITERAL",
            "AND",
            "UNQUOTED_IDENTIFIER",
            "LT",
            "NUMBER_LITERAL",
            "OR",
            "UNQUOTED_IDENTIFIER",
            "GT",
            "NUMBER_LITERAL",
            "SEMI",
        ],
    },
    {
        "name": "Test A11: Bitwise operators",
        "query": "SELECT a & b, c | d, e ^ f FROM t;",
        "expected": [
            "SELECT",
            "UNQUOTED_IDENTIFIER",
            "AMPERSAND",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "PIPE",
            "UNQUOTED_IDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "CARET",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test A12: Line and nested block comments",
        "query": """
            -- leading line comment
            SELECT 1 /* outer
                /* nested level 1 */
                still in outer
            */ , 2 -- trailing
            FROM t; /* last */ 
        """,
        "expected": [
            "SELECT",
            "NUMBER_LITERAL",
            "COMMA",
            "NUMBER_LITERAL",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test A13: Data types coverage",
        "query": """
            CREATE TABLE T (
                c1 BIGINT,
                c2 BINARY,
                c3 BIT,
                c4 CHAR,
                c5 DATE,
                c6 DECIMAL,
                c7 FLOAT,
                c8 INT,
                c9 MONEY,
                c10 NCHAR,
                c11 NUMERIC,
                c12 NVARCHAR,
                c13 REAL,
                c14 SMALLINT,
                c15 TEXT,
                c16 TIME,
                c17 TIMESTAMP,
                c18 TINYINT,
                c19 UNIQUEIDENTIFIER,
                c20 VARBINARY,
                c21 VARCHAR,
                c22 XML
            );
        """,
        "expected": [
            "CREATE",
            "TABLE",
            "UNQUOTED_IDENTIFIER",
            "LPAREN",
            "UNQUOTED_IDENTIFIER",
            "BIGINT",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "BINARY",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "BIT",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "CHAR",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "DATE",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "DECIMAL_TYPE",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "FLOAT_TYPE",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "INT_TYPE",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "MONEY",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "NCHAR",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "NUMERIC",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "NVARCHAR",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "REAL",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "SMALLINT",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "TEXT",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "TIME",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "TIMESTAMP",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "TINYINT",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "UNIQUEIDENTIFIER",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "VARBINARY",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "VARCHAR",
            "COMMA",
            "UNQUOTED_IDENTIFIER",
            "XML",
            "RPAREN",
            "SEMI",
        ],
    },
    {
        "name": "Test A14: Special SQL keywords and clauses",
        "query": """
            SELECT DISTINCT TOP 10 WITH TIES col
            FROM T
            WITH (NOLOCK)
            WHERE col BETWEEN 1 AND 100
            GROUP BY col
            HAVING COUNT(*) > 1
            ORDER BY col DESC;
        """,
        "expected": [
            "SELECT",
            "DISTINCT",
            "TOP",
            "NUMBER_LITERAL",
            "WITH",
            "UNQUOTED_IDENTIFIER",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "WITH",
            "LPAREN",
            "UNQUOTED_IDENTIFIER",
            "RPAREN",
            "WHERE",
            "UNQUOTED_IDENTIFIER",
            "BETWEEN",
            "NUMBER_LITERAL",
            "AND",
            "NUMBER_LITERAL",
            "GROUP",
            "BY",
            "UNQUOTED_IDENTIFIER",
            "HAVING",
            "COUNT",
            "LPAREN",
            "STAR",
            "RPAREN",
            "GT",
            "NUMBER_LITERAL",
            "ORDER",
            "BY",
            "UNQUOTED_IDENTIFIER",
            "DESC",
            "SEMI",
        ],
    },
    {
        "name": "Test A15: Window and analytic-related keywords",
        "query": "SELECT COUNT(*) FILTER (WHERE col > 0) OVER (PARTITION BY col ORDER BY col ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) FROM t;",
        "expected": [
            "SELECT",
            "COUNT",
            "LPAREN",
            "STAR",
            "RPAREN",
            "FILTER",
            "LPAREN",
            "WHERE",
            "UNQUOTED_IDENTIFIER",
            "GT",
            "NUMBER_LITERAL",
            "RPAREN",
            "OVER",
            "LPAREN",
            "PARTITION",
            "BY",
            "UNQUOTED_IDENTIFIER",
            "ORDER",
            "BY",
            "UNQUOTED_IDENTIFIER",
            "ROWS",
            "BETWEEN",
            "NUMBER_LITERAL",
            "UNQUOTED_IDENTIFIER",
            "AND",
            "CURRENT",
            "ROW",
            "RPAREN",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test A16: INTERVAL and date parts",
        "query": "SELECT INTERVAL '1' DAY, INTERVAL '2' MONTH, INTERVAL '3' YEAR FROM t;",
        "expected": [
            "SELECT",
            "INTERVAL",
            "STRING_LITERAL",
            "DAY",
            "COMMA",
            "INTERVAL",
            "STRING_LITERAL",
            "MONTH",
            "COMMA",
            "INTERVAL",
            "STRING_LITERAL",
            "YEAR",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test A17: OFFSET, LIMIT and ONLY",
        "query": "SELECT * FROM t ORDER BY id LIMIT 10 OFFSET 5 ROWS ONLY;",
        "expected": [
            "SELECT",
            "STAR",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "ORDER",
            "BY",
            "UNQUOTED_IDENTIFIER",
            "LIMIT",
            "NUMBER_LITERAL",
            "OFFSET",
            "NUMBER_LITERAL",
            "ROWS",
            "ONLY",
            "SEMI",
        ],
    },
    {
        "name": "Test A18: Complex UNION/EXCEPT/INTERSECT",
        "query": "SELECT id FROM t1 UNION ALL SELECT id FROM t2 EXCEPT SELECT id FROM t3 INTERSECT SELECT id FROM t4;",
        "expected": [
            "SELECT",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "UNION",
            "ALL",
            "SELECT",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "EXCEPT",
            "SELECT",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "INTERSECT",
            "SELECT",
            "UNQUOTED_IDENTIFIER",
            "FROM",
            "UNQUOTED_IDENTIFIER",
            "SEMI",
        ],
    },
    {
        "name": "Test A19: Whitespace and empty input edge cases",
        "query": "   \n\t  -- only comment\n  /* block comment */  ",
        "expected": [
            # No tokens at all
        ],
    },
    {
        "name": "Test A20: Minimal single-token statements",
        "query": "SELECT; FROM; WHERE; AND; OR; NOT;",
        "expected": [
            "SELECT",
            "SEMI",
            "FROM",
            "SEMI",
            "WHERE",
            "SEMI",
            "AND",
            "SEMI",
            "OR",
            "SEMI",
            "NOT",
            "SEMI",
        ],
    },
]


def tokenize_query(query):
    """Tokenize a SQL query and return list of token types"""
    input_stream = InputStream(query)
    lexer = SQLLexer(input_stream)
    tokens = lexer.getAllTokens()

    token_list = []
    for token in tokens:
        token_type_name = lexer.symbolicNames[token.type]
        token_list.append(
            {
                "type": token_type_name,
                "text": token.text,
                "line": token.line,
                "column": token.column,
            }
        )

    return token_list
 

def run_test(test_case):
    """Run a single test case"""
    query = test_case["query"]
    expected = test_case["expected"]
    name = test_case["name"]

    print(f"\n{'='*70}")
    print(f"{name}")
    print(f"{'='*70}")
    print(f"Query: {query}")
    print(f"\nExpected tokens: {len(expected)}")

    try:
        tokens = tokenize_query(query)
        actual = [t["type"] for t in tokens]

        print(f"Actual tokens:   {len(actual)}")

        # Compare results
        passed = True
        if len(expected) != len(actual):
            print(f"\n❌ FAILED: Token count mismatch!")
            passed = False
        else:
            for i, (exp, act) in enumerate(zip(expected, actual)):
                if exp != act:
                    print(f"\n❌ FAILED at position {i}:")
                    print(f"   Expected: {exp}")
                    print(f"   Actual:   {act}")
                    passed = False
                    break

        if passed:
            print(f"\n✅ PASSED")

        # Print detailed token information
        print(f"\nDetailed tokens:")
        for i, token in enumerate(tokens):
            status = "✓" if i < len(expected) and token["type"] == expected[i] else "✗"
            expected_token = expected[i] if i < len(expected) else "N/A"
            print(
                f"  {status} [{i}] {token['type']:25s} '{token['text']:20s}' (Expected: {expected_token})"
            )

        return passed

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def run_all_tests():
    """Run all test cases"""
    print("=" * 70)
    print("SQL LEXER TEST SUITE")
    print("=" * 70)

    results = []
    for test_case in TEST_CASES:
        result = run_test(test_case)
        results.append((test_case["name"], result))

    # Summary
    print(f"\n{'='*70}")
    print("TEST SUMMARY")
    print(f"{'='*70}")

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status}: {name}")

    print(f"\n{passed}/{total} tests passed ({passed/total*100:.1f}%)")

    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
