import lexer as lp
from parser import Token, Parser, print_ast, ParserError


# Output sample 1: 1+2*3
print("\n\nOutput Sample 1: 1+2*3\n")
#tokens with lexer
print("Tokens:")
result = lp.run('<stdin', '1+2*3')
if result:
    print(f'\n{result}\n')

#AST with parser
print("Abstract Syntax Tree (AST):")
tokens = [
    Token(Token.INTEGER, 1),
    Token("PLUS", "+"),
    Token(Token.INTEGER, 2),
    Token("MUL", "*"),
    Token(Token.INTEGER, 3),
    Token(Token.EOF, None)
]

parser = Parser(tokens)
ast = parser.expression()
print_ast(ast)



# Output sample 2: (1+4)*5+1
print("\n\n\nOutput Sample 2: (1+4)*5+1\n")
#tokens with lexer
print("Tokens:")
result = lp.run('<stdin', '(1+4)*5+1')
if result:
    print(f'\n{result}\n')

#AST with parser
print("Abstract Syntax Tree (AST):")
tokens = [
    Token("LPAREN", "("),
    Token(Token.INTEGER, 1),
    Token("PLUS", "+"),
    Token(Token.INTEGER, 4),
    Token("RPAREN", ")"),
    Token("MUL", "*"),
    Token(Token.INTEGER, 5),
    Token("PLUS", "+"),
    Token(Token.INTEGER, 1),
    Token(Token.EOF, None)
]

parser = Parser(tokens)
ast = parser.expression()
print_ast(ast)



#Output sample 3: 3+)
print("\n\n\nOutput Sample 2: 3+)\n")
#tokens with lexer
print("Tokens:")
result = lp.run('<stdin', '3+)')
if result:
    print(f'\n{result}\n')

#AST with parser
print("Abstract Syntax Tree (AST):")
tokens = [
    Token(Token.INTEGER, 3),
    Token("PLUS", "+"),
    Token("RPAREN", ")"),
    Token(Token.EOF, None)
]
try:
    parser = Parser(tokens)
    ast = parser.expression()
    print_ast(ast)
except ParserError as e:
    print(f'Parser Error: {e}')

