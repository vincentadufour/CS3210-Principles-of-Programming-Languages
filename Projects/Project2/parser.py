class ASTNode:
    pass



class Token:
    INTEGER, EOF, LPAREN, RPAREN = 'INTEGER', 'EOF', 'LPAREN', 'RPAREN'
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"'{self.value}'"



class NumberNode(ASTNode):
    def __init__(self, token):
        self.token = token
        self.value = token.value
    def __repr__(self):

        return f"Number({self.value})"
    

# for returning parsing errors
class ParserError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Syntax Error: {self.message}"



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

    # raises ParserError if factor fails if statement
    def factor(self):
        token = self.current_token
        if token.type == Token.INTEGER:
            self.consume_token(Token.INTEGER)
            return NumberNode(token)
        elif token.type == Token.LPAREN:
            self.consume_token(Token.LPAREN)
            node = self.expression()
            self.consume_token(Token.RPAREN)
            return node
        else:
            raise ParserError(f"Unexpected token '{token.value}'")
    
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
        print(f"{indent}BinOp {node.op}")
        print(indent, "Left:")
        print_ast(node.left, indent + "  ")
        print(indent, "Right:")
        print_ast(node.right, indent + "  ")

    
