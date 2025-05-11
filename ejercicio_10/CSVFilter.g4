grammar CSVFilter;

prog: stat+ ;

stat
    : loadStat
    | filterStat
    | countStat
    | printStat
    | countBetweenStat 
    ;

loadStat: 'load' STRING ';' ;
filterStat: 'filter' 'column' STRING OPERATOR NUMBER ';' ;
countStat: 'count' 'column' STRING OPERATOR NUMBER ';' ;
printStat: 'print' ';' ;
countBetweenStat: 'count' 'column' STRING 'between' NUMBER 'and' NUMBER ';' ;

// 🔥 Soportar operadores lógicos
OPERATOR: '>=' | '<=' | '>' | '<' | '==' | '!=' ;

// 🔥 Soportar números decimales o enteros
STRING: '"' (~["\r\n])* '"' ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;

WS: [ \t\r\n]+ -> skip ;