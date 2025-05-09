# Author: Vincent Dufour
# Date: 27.03.2025
# Time Taken: 6 hours and 45 minutes



import lexer as lp
from parser import Token, Parser, print_ast, ParserError


print("\n------ TEST CASES ------\n")



# Test Case 1: 1+2*3  |  Operator Order
print("\n\nTest Case 1: 1+2*3  |  Operator Order\n")
# tokens with lexer
print("Tokens:")
result = lp.run('<stdin', '1+2*3')
if result:
    print(f'\n{result}\n')

# AST with parser
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



# Test Case 2: (1+4)*5+1  |  Parentheses
print("\n\n\nTest Case 2: (1+4)*5+1  |  Parentheses\n")
# tokens with lexer
print("Tokens:")
result = lp.run('<stdin', '(1+4)*5+1')
if result:
    print(f'\n{result}\n')

# AST with parser
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



# Test Case 3: 3+)  |  Unmatched Parentheses
print("\n\n\nTest Case 3: 3+)  |  Unmatched Parentheses\n")
# tokens with lexer
print("Tokens:")
result = lp.run('<stdin', '3+)')
if result:
    print(f'\n{result}\n')

# AST with parser
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



# Test Case 4: Floating Point
print("\n\n\nTest Case 4: 3.14 * 2  |  Floating point numbers\n")
# tokens with lexer
print("Tokens:")
result = lp.run('<stdin', '3.14 * 2')
if result:
    print(f'\n{result}\n')

# AST with parser
print("Abstract Syntax Tree (AST):")
tokens = [
    Token(Token.FLOAT, 3.14),
    Token("MUL", "*"),
    Token(Token.INTEGER, 2),
    Token(Token.EOF, None)
]
try:
    parser = Parser(tokens)
    ast = parser.expression()
    print_ast(ast)
except ParserError as e:
    print(f'Parser Error: {e}')



# Test Case 5: Unary Operator
print("\n\n\nTest Case 5: -7  |  Unary Operator\n")
# tokens with lexer
print("Tokens:")
result = lp.run('<stdin', '-7')
if result:
    print(f'\n{result}\n')

# AST with parser
print("Abstract Syntax Tree (AST):")
tokens = [
    Token("MINUS", "-"),
    Token(Token.FLOAT, 7),
    Token(Token.EOF, None)
]
try:
    parser = Parser(tokens)
    ast = parser.expression()
    print_ast(ast)
except ParserError as e:
    print(f'Parser Error: {e}')
