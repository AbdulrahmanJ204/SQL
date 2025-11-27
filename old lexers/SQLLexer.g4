lexer grammar SQLLexer;

// ============================================================================
// RESERVED WORDS (Table D-1)
// ============================================================================

ALL         : A L L;
ALTER       : A L T E R;
AND         : A N D;
ANY         : A N Y;
AS          : A S;
ASC         : A S C;
AT          : A T;

BEGIN       : B E G I N;
BETWEEN     : B E T W E E N;
BY          : B Y;

CASE        : C A S E;
CHECK       : C H E C K;
CLUSTERS    : C L U S T E R S;
CLUSTER     : C L U S T E R;
COLAUTH     : C O L A U T H;
COLUMNS     : C O L U M N S;
COMPRESS    : C O M P R E S S;
CONNECT     : C O N N E C T;
CRASH       : C R A S H;
CREATE      : C R E A T E;
CURSOR      : C U R S O R;

DECLARE     : D E C L A R E;
DEFAULT     : D E F A U L T;
DESC        : D E S C;
DISTINCT    : D I S T I N C T;
DROP        : D R O P;

ELSE        : E L S E;
END         : E N D;
EXCEPTION   : E X C E P T I O N;
EXCLUSIVE   : E X C L U S I V E;

FETCH       : F E T C H;
FOR         : F O R;
FROM        : F R O M;
FUNCTION    : F U N C T I O N;

GOTO        : G O T O;
GRANT       : G R A N T;
GROUP       : G R O U P;

HAVING      : H A V I N G;

IDENTIFIED  : I D E N T I F I E D;
IF          : I F;
IN          : I N;
INDEX       : I N D E X;
INDEXES     : I N D E X E S;
INSERT      : I N S E R T;
INTERSECT   : I N T E R S E C T;
INTO        : I N T O;
IS          : I S;

LIKE        : L I K E;
LOCK        : L O C K;

MINUS       : M I N U S;
MODE        : M O D E;

NOCOMPRESS  : N O C O M P R E S S;
NOT         : N O T;
NOWAIT      : N O W A I T;
NULL        : N U L L;

OF          : O F;
ON          : O N;
OPTION      : O P T I O N;
OR          : O R;
ORDER       : O R D E R;
OVERLAPS    : O V E R L A P S;

PROCEDURE   : P R O C E D U R E;
PUBLIC      : P U B L I C;

RESOURCE    : R E S O U R C E;
REVOKE      : R E V O K E;

SELECT      : S E L E C T;
SHARE       : S H A R E;
SIZE        : S I Z E;
SQL         : S Q L;
START       : S T A R T;
SUBTYPE     : S U B T Y P E;

TABAUTH     : T A B A U T H;
TABLE       : T A B L E;
THEN        : T H E N;
TO          : T O;
TYPE        : T Y P E;

UNION       : U N I O N;
UNIQUE      : U N I Q U E;
UPDATE      : U P D A T E;

VALUES      : V A L U E S;
VIEW        : V I E W;
VIEWS       : V I E W S;

WHEN        : W H E N;
WHERE       : W H E R E;
WITH        : W I T H;

// ============================================================================
// KEYWORDS (Table D-2)
// ============================================================================


ADD                 : A D D;
ACCESSIBLE          : A C C E S S I B L E;
AGENT               : A G E N T;
AGGREGATE           : A G G R E G A T E;
ARRAY               : A R R A Y;
ATTRIBUTE           : A T T R I B U T E;
AUTHID              : A U T H I D;
AVG                 : A V G;

BFILE_BASE          : B F I L E '_' B A S E;
BINARY              : B I N A R Y;
BLOB_BASE           : B L O B '_' B A S E;
BLOCK               : B L O C K;
BODY                : B O D Y;
BOTH                : B O T H;
BOUND               : B O U N D;
BULK                : B U L K;
BYTE                : B Y T E;


CALL                : C A L L;
CALLING             : C A L L I N G;
CASCADE             : C A S C A D E;
CHAR                : C H A R;
CHAR_BASE           : C H A R '_' B A S E;
CHARACTER           : C H A R A C T E R;
CHARSET             : C H A R S E T;
CHARSETFORM         : C H A R S E T F O R M;
CHARSETID           : C H A R S E T I D;
CLOB_BASE           : C L O B '_' B A S E;
CLONE               : C L O N E;
CLOSE               : C L O S E;
COLLECT             : C O L L E C T;
COMMENT             : C O M M E N T;
COMMIT              : C O M M I T;
COMMITTED           : C O M M I T T E D;
COMPILED            : C O M P I L E D;
CONSTANT            : C O N S T A N T;
CONSTRUCTOR         : C O N S T R U C T O R;
CONTEXT             : C O N T E X T;
CONTINUE            : C O N T I N U E;
CONVERT             : C O N V E R T;
COUNT               : C O U N T;
CREDENTIAL          : C R E D E N T I A L;
CURRENT             : C U R R E N T;
CUSTOMDATUM         : C U S T O M D A T U M;

DANGLING            : D A N G L I N G;
DATA                : D A T A;
DATE                : D A T E;
DATE_BASE           : D A T E '_' B A S E;
DAY                 : D A Y;
DEFINE              : D E F I N E;
DELETE              : D E L E T E;
DETERMINISTIC       : D E T E R M I N I S T I C;
DIRECTORY           : D I R E C T O R Y;
DOUBLE              : D O U B L E;
DURATION            : D U R A T I O N;

ELEMENT             : E L E M E N T;
ELSIF               : E L S I F;
EMPTY               : E M P T Y;
ESCAPE              : E S C A P E;
EXCEPT              : E X C E P T;
EXCEPTIONS          : E X C E P T I O N S;
EXECUTE             : E X E C U T E;
EXISTS              : E X I S T S;
EXIT                : E X I T;
EXTERNAL            : E X T E R N A L;

FINAL               : F I N A L;
FIRST               : F I R S T;
FIXED               : F I X E D;
FLOAT               : F L O A T;
FORALL              : F O R A L L;
FORCE               : F O R C E;

GENERAL             : G E N E R A L;

HASH                : H A S H;
HEAP                : H E A P;
HIDDEN_KEYWORD      : H I D D E N;
HOUR                : H O U R;

IMMEDIATE           : I M M E D I A T E;
IMMUTABLE           : I M M U T A B L E;
INCLUDING           : I N C L U D I N G;
INDICATOR           : I N D I C A T O R;
INDICES             : I N D I C E S;
INFINITE            : I N F I N I T E;
INSTANTIABLE        : I N S T A N T I A B L E;
INT                 : I N T;
INTERFACE           : I N T E R F A C E;
INTERVAL            : I N T E R V A L;
INVALIDATE          : I N V A L I D A T E;
ISOLATION           : I S O L A T I O N;

JAVA                : J A V A;

LANGUAGE            : L A N G U A G E;
LARGE               : L A R G E;
LEADING             : L E A D I N G;
LENGTH              : L E N G T H;
LEVEL               : L E V E L;
LIBRARY             : L I B R A R Y;
LIKE2               : L I K E '2';
LIKE4               : L I K E '4';
LIKEC               : L I K E C;
LIMIT               : L I M I T;
LIMITED             : L I M I T E D;
LOCAL               : L O C A L;
LONG                : L O N G;
LOOP                : L O O P;

MAP                 : M A P;
MAX                 : M A X;
MAXLEN              : M A X L E N;
MEMBER              : M E M B E R;
MERGE               : M E R G E;
MIN                 : M I N;
MINUTE              : M I N U T E;
MOD                 : M O D;
MODIFY              : M O D I F Y;
MONTH               : M O N T H;
MULTISET            : M U L T I S E T;
MUTABLE             : M U T A B L E;

NAME                : N A M E;
NAN                 : N A N;
NATIONAL            : N A T I O N A L;
NATIVE              : N A T I V E;
NCHAR               : N C H A R;
NEW                 : N E W;
NOCOPY              : N O C O P Y;
NUMBER_BASE         : N U M B E R '_' B A S E;

OBJECT              : O B J E C T;
OCICOLL             : O C I C O L L;
OCIDATE             : O C I D A T E;
OCIDATETIME         : O C I D A T E T I M E;
OCIDURATION         : O C I D U R A T I O N;
OCIINTERVAL         : O C I I N T E R V A L;
OCILOBLOCATOR       : O C I L O B L O C A T O R;
OCINUMBER           : O C I N U M B E R;
OCIRAW              : O C I R A W;
OCIREF              : O C I R E F;
OCIREFCURSOR        : O C I R E F C U R S O R;
OCIROWID            : O C I R O W I D;
OCISTRING           : O C I S T R I N G;
OCITYPE             : O C I T Y P E;
OLD                 : O L D;
ONLY                : O N L Y;
OPAQUE              : O P A Q U E;
OPEN                : O P E N;
OPERATOR            : O P E R A T O R;
ORACLE              : O R A C L E;
ORADATA             : O R A D A T A;
ORGANIZATION        : O R G A N I Z A T I O N;
ORLANY              : O R L A N Y;
ORLVARY             : O R L V A R Y;
OTHERS              : O T H E R S;
OUT                 : O U T;
OVERRIDING          : O V E R R I D I N G;

PACKAGE             : P A C K A G E;
PARALLEL_ENABLE     : P A R A L L E L '_' E N A B L E;
PARAMETER           : P A R A M E T E R;
PARAMETERS          : P A R A M E T E R S;
PARENT              : P A R E N T;
PARTITION           : P A R T I T I O N;
PASCAL              : P A S C A L;
PERSISTABLE         : P E R S I S T A B L E;
PIPE                : P I P E;
PIPELINED           : P I P E L I N E D;
PLUGGABLE           : P L U G G A B L E;
POLYMORPHIC         : P O L Y M O R P H I C;
PRAGMA              : P R A G M A;
PRECISION           : P R E C I S I O N;
PRIOR               : P R I O R;
PRIVATE             : P R I V A T E;

RAISE               : R A I S E;
RANGE               : R A N G E;
RAW                 : R A W;
READ                : R E A D;
RECORD              : R E C O R D;
REF                 : R E F;
REFERENCE           : R E F E R E N C E;
RELIES_ON           : R E L I E S '_' O N;
REM                 : R E M;
REMAINDER           : R E M A I N D E R;
RENAME              : R E N A M E;
RESULT              : R E S U L T;
RESULT_CACHE        : R E S U L T '_' C A C H E;
RETURN              : R E T U R N;
RETURNING           : R E T U R N I N G;
REVERSE             : R E V E R S E;
ROLLBACK            : R O L L B A C K;
ROW                 : R O W;

SAMPLE              : S A M P L E;
SAVE                : S A V E;
SAVEPOINT           : S A V E P O I N T;
SB1                 : S B '1';
SB2                 : S B '2';
SB4                 : S B '4';
SECOND              : S E C O N D;
SEGMENT             : S E G M E N T;
SELF                : S E L F;
SEPARATE            : S E P A R A T E;
SEQUENCE            : S E Q U E N C E;
SERIALIZABLE        : S E R I A L I Z A B L E;
SET                 : S E T;
SHORT               : S H O R T;
SIZE_T              : S I Z E '_' T;
SOME                : S O M E;
SPARSE              : S P A R S E;
SQLCODE             : S Q L C O D E;
SQLDATA             : S Q L D A T A;
SQLNAME             : S Q L N A M E;
SQLSTATE            : S Q L S T A T E;
STANDARD            : S T A N D A R D;
STATIC              : S T A T I C;
STDDEV              : S T D D E V;
STORED              : S T O R E D;
STRING              : S T R I N G;
STRUCT              : S T R U C T;
STYLE               : S T Y L E;
SUBMULTISET         : S U B M U L T I S E T;
SUBPARTITION        : S U B P A R T I T I O N;
SUBSTITUTABLE       : S U B S T I T U T A B L E;
SUM                 : S U M;
SYNONYM             : S Y N O N Y M;

TDO                 : T D O;
THE                 : T H E;
TIME                : T I M E;
TIMESTAMP           : T I M E S T A M P;
TIMEZONE_ABBR       : T I M E Z O N E '_' A B B R;
TIMEZONE_HOUR       : T I M E Z O N E '_' H O U R;
TIMEZONE_MINUTE     : T I M E Z O N E '_' M I N U T E;
TIMEZONE_REGION     : T I M E Z O N E '_' R E G I O N;
TRAILING            : T R A I L I N G;
TRANSACTION         : T R A N S A C T I O N;
TRANSACTIONAL       : T R A N S A C T I O N A L;
TRUSTED             : T R U S T E D;

UB1                 : U B '1';
UB2                 : U B '2';
UB4                 : U B '4';
UNDER               : U N D E R;
UNPLUG              : U N P L U G;
UNSIGNED            : U N S I G N E D;
UNTRUSTED           : U N T R U S T E D;
USE                 : U S E;
USING               : U S I N G;

VALIST              : V A L I S T;
VALUE               : V A L U E;
VARIABLE            : V A R I A B L E;
VARIANCE            : V A R I A N C E;
VARRAY              : V A R R A Y;
VARYING             : V A R Y I N G;
VOID                : V O I D;

WHILE               : W H I L E;
WORK                : W O R K;
WRAPPED             : W R A P P E D;
WRITE               : W R I T E;

YEAR                : Y E A R;

// ============================================================================
// DELIMITERS (Table 3-2)
// ============================================================================

// Multi-character operators (must come before single-character)
ASSIGNMENT          : ':=';
ASSOCIATION         : '=>';
CONCAT              : '||';
EXPONENT            : '**';
LABEL_BEGIN         : '<<';
LABEL_END           : '>>';
COMMENT_BEGIN       : '/*';
COMMENT_END         : '*/';
RANGEOP               : '..';
NOT_EQUAL           : '<>' | '!=' | '~=' | '^=';
LESS_EQUAL          : '<=';
GREATER_EQUAL       : '>=';
COMMENT_LINE        : '--';

// Single-character operators and delimiters
PLUS                : '+' ;
MINUSOP             : '-' ;
STAR                : '*' ;
SLASH               : '/' ;
PERCENT             : '%' ;
LPAREN              : '(' ;
RPAREN              : ')' ;
COLON               : ':' ;
COMMA               : ',' ;
SEMICOLON           : ';' ;
DOT                 : '.' ;
EQUAL               : '=' ;
LESS_THAN           : '<' ;
GREATER_THAN        : '>' ;
AT_SIGN             : '@' ;
SINGLE_QUOTE        : '\'';
DOUBLE_QUOTE        : '"' ;

// ============================================================================
// LITERALS
// ============================================================================

// Numeric literals
NUMERIC_LITERAL
    : DIGIT+ ('.' DIGIT+)? (E [+-]? DIGIT+)?
    | '.' DIGIT+ (E [+-]? DIGIT+)?
    ;

// String literals
STRING_LITERAL
    : '\'' (~'\'' | '\'\'')* '\''
    ;

// Quoted identifiers
QUOTED_IDENTIFIER
    : '"' (~'"' | '""')+ '"'
    ;

// Regular identifiers
ORDINARY_IDENTIFIER
    : ALPHA [a-zA-Z0-9_$#]*
    ;

// ============================================================================
// COMMENTS AND WHITESPACE
// ============================================================================

// Single-line comment
SINGLE_LINE_COMMENT
    : '--' ~[\r\n]* -> skip
    ;

// Multi-line comment
MULTI_LINE_COMMENT
    : '/*' .*? '*/' -> skip
    ;

// Whitespace
WS
    : [ \t\r\n]+ -> skip
    ;

// ============================================================================
// CASE-INSENSITIVE FRAGMENTS
// ============================================================================

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

fragment DIGIT : [0-9];
fragment ALPHA : [a-zA-Z];