// CSV.g4
grammar CSV;

csvFile : header row+ ;
header  : row ;
row     : field (',' field)* '\r'? '\n' ;
field   : TEXT   # text
        | STRING # string
        |        # empty ;

TEXT   : ~[",\n\r]+ ;
STRING : '"' ('""' | ~'"')* '"' ;
WS     : [ \t]+ -> skip ;
