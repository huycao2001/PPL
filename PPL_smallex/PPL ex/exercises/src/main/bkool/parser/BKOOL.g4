grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : EOF ;

ID: [a-z][a-z0-9]* ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: ~[a-z0-9\t\r\n ];
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;