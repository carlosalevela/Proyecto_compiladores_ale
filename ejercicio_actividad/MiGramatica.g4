grammar MiGramatica;

// Regla principal: permite múltiples sentencias terminadas en ';'
programa: (sentencia ';')+ EOF ;

// Sentencias permitidas
sentencia
    : forLoop  
    | asignacion  
    ;

// Regla para `for`
forLoop
    : 'for' '(' asignacion ';' condicion ';' asignacion ')' '{' (sentencia (';')?)* '}' # ForStatement
    ;

// Condiciones dentro del `for`
condicion
    : ID op=('>' | '<' | '==' | '!=') INT  # CondicionSimple
    ;

// Asignaciones con `=`
asignacion
    : ID '=' expresion # Assign
    ;

// Expresiones matemáticas con prioridad de operadores
expresion
    : expresion op=('*'|'/') expresion     # MulDiv
    | expresion op=('+'|'-') expresion     # AddSub
    | INT                                  # Int
    | ID                                   # Variable
    | '(' expresion ')'                    # Parens
    ;

// Reglas léxicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT : [0-9]+ ;                   // Números enteros
WS  : [ \t\r\n]+ -> skip ;       // Ignorar espacios en blanco
