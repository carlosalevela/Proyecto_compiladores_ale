grammar Simple;

prog: classDef+ ;

classDef
    : 'class' ID '{' member+ '}' 
    ;

member
    : 'int' ID ';'
    | 'int' ID '(' ID ')' '{' stat '}' 
    ;

stat
    : expr ';'
    | ID '=' expr ';'
    ;

expr
    : expr op=('*'|'/') expr        # MultiDiv
    | expr op=('+'|'-') expr        # SumaResta
    | ID '(' INT ')'                # FuncCall
    | INT                           # Int
    | ID                            # Var
    | '(' expr ')'                  # Parens
    ;

INT : [0-9]+ ;
ID  : [a-zA-Z]+ ;
WS  : [ \t\r\n]+ -> skip ;