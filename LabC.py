import ctypes

# Load the shared library containing the YAL-generated lexer
lib = ctypes.CDLL('ejemplo.yal')

# Define the token types
TOK_IDENTIFIER = 1
TOK_NUMBER = 2
# ...

# Define the lexer callback function
def yylex():
    token_type = lib.yylex()
    if token_type == TOK_IDENTIFIER:
        return ('IDENTIFIER', lib.yytext)
    elif token_type == TOK_NUMBER:
        return ('NUMBER', float(lib.yytext))
    # ...

# Initialize the lexer
lib.yyrestart(ctypes.c_void_p(0))
lib.yylineno = 1

# Tokenize input text
input_text = 'some input text'
while True:
    token = yylex()
    if not token:
        break
    print(token)
