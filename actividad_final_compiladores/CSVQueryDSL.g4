grammar CSVQueryDSL;

prog: stat+ ;

stat
    : loadStat
    | filterStat
    | aggregateStat
    | printStat
    ;

loadStat: 'load' STRING ';' ;

filterStat: 'filter' filterExprList ';' ;
filterExprList: filterExpr (LOGICAL_OP filterExpr)* ;
filterExpr: 'column' STRING OPERATOR value ;

aggregateStat: 'aggregate' aggregateFunction 'column' STRING ';' ;
aggregateFunction: 'count' | 'sum' | 'average' ;

printStat: 'print' ';' ;

// --- Valores posibles ---
value: NUMBER | STRING ;

// --- Tokens ---
OPERATOR: '>=' | '<=' | '>' | '<' | '==' | '!=' ;
LOGICAL_OP: 'AND' | 'OR' ;

STRING: '"' (~["\r\n])* '"' ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;

WS: [ \t\r\n]+ -> skip ;
