class ASTNode:
    pass

class Token:
    INTEGER, EOF = 'INTEGER', 'EOF'
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class NumberNode(ASTNode):
    def __init__(self, token):
        self.token = token
        self.value = token.value
    def __repr__(self):

        return f"Number({self.value})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def consume_token(self, token_type):
        if self.current_token.type == token_type:
            self.pos += 1
            if self.pos < len(self.tokens):
                self.current_token = self.tokens[self.pos]
            else:
                self.current_token = Token(Token.EOF, None)
        else:
            raise Exception(f"Unexpected token {self.current_token.type}, expected {token_type}")

    def factor(self):
        token = self.current_token
        if token.type == Token.INTEGER:
            self.consume_token(Token.INTEGER)
            return NumberNode(token)
        raise Exception("Invalid factor")
    
    def term(self):
        left = self.factor()
        while self.current_token.type in ('MUL', 'DIV'):
            op_token = self.current_token
            self.consume_token(op_token.type)
            right = self.factor()
            left = BiOpNode(left, op_token, right)
        return left
    
    def expression(self):
        left = self.term()
        while self.current_token.type in ('PLUS', 'MINUS'):
            op_token = self.current_token
            self.consume_token(op_token.type)
            right = self.term()
            left = BiOpNode(left, op_token, right)
        return left
    
##############
    
class BiOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op.value} {self.right})"
    
    

def print_ast(node, indent=""):
    if isinstance(node, NumberNode):
        print(f"{indent}Num({node.value})")
    elif isinstance(node, BiOpNode):
        print(f"{indent}BinOp({node.op})")
        print(indent, "Left:")
        print_ast(node.left, indent + "  ")
        print(indent, "Right:")
        print_ast(node.right, indent + "  ")

    



# Step 1
#  Parsing just a number (e.g., "1")
tokens = [Token(Token.INTEGER, 1), Token(Token.EOF, None)]
parser = Parser(tokens)
ast = parser.factor()
print(f"\nStep 1: {ast}")  # Expected output: Number(1)


# Step 2
#  Test case: Parsing "2 * 3"
tokens = [
    Token(Token.INTEGER, 2),
    Token("MUL", "*"),
    Token(Token.INTEGER, 3),
    Token(Token.EOF, None)
]

parser = Parser(tokens)
ast = parser.term()
print(f"\nStep 2: {ast}")  # Expected output: (Number(2) * Number(3))


# Step 3.1
# Test case: Parsing "1 + 2 * 3"
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
print(f"\nStep 3.1: {ast}")  # Expected output: (Number(1) + (Number(2) * Number(3)))


# Step 3.2
# AST Tree Printing
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
print("\nStep 3.2:")
print_ast(ast)




# Step 4.1
# 4 + 5 * 6 - 7 and it's swapped form 4 * 5 + 6 - 7,
tokens = [
    Token(Token.INTEGER, 4),
    Token("PLUS", "+"),
    Token(Token.INTEGER, 5),
    Token("MUL", "*"),
    Token(Token.INTEGER, 6), 
    Token("MINUS", "-"),
    Token(Token.INTEGER, 7),
    Token(Token.EOF, None)
]

parser = Parser(tokens)
ast = parser.expression()
print(f"\nStep 4.1:")
print_ast(ast)


# Step 4.2
tokens = [
    Token(Token.INTEGER, 4),
    Token("MUL", "*"),
    Token(Token.INTEGER, 5),
    Token("PLUS", "+"),
    Token(Token.INTEGER, 6), 
    Token("MINUS", "-"),
    Token(Token.INTEGER, 7),
    Token(Token.EOF, None)
]

parser = Parser(tokens)
ast = parser.expression()
print(f"\nStep 4.2:")
print_ast(ast)

