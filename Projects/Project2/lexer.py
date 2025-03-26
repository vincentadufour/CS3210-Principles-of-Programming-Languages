#Create TOCKENS list
INT  = 'INT'
FLOAT = 'FLOAT'
PLUS  = 'PLUS'
MINUS = 'MINUS'
DIVIDE = 'DIVIDE'
MUL = 'MUL'
OPEN_PAR = 'LPAREN'
CLOSE_PAR = 'RPAREN'
COMMENT = 'COMMENT'

# create illegal characters
ILLEGAL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Create number list
DIGITS = '0123456789'

#Create Operators list
OPERATORS = '+-/*()'

# creates comment
COMMENT = "!"

#Create a Tocken Class as given below
class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value})"

#Create a lexer class constructor as below
class Lexer:
    def __init__(self, fn, text):
        self.fn = fn    
        self.text = text
        self.pos = -1 
        self.current_char = None
        self.column_pos = -1
        self.line_pos = 0
        self.advance()
        
        
# moves through characters
    def advance(self):
        self.pos += 1

        if self.current_char != '\n':
            self.column_pos += 1
        else:
            self.column_pos = 0
            self.line_pos += 1

        if self.pos < len(self.text):
            self.current_char=self.text[self.pos]
        else:
            self.current_char=None
            

# token decision tree
    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in OPERATORS:
                tokens.append(self.make_operater())
            elif self.current_char in DIGITS: 
                tokens.append(self.make_number())
            elif self.current_char in COMMENT:
                tokens.append(self.skip_line())
            elif self.current_char == "\n":
                self.advance()

            # decided to make both error statements stop reading and Not deliver a full token instead of having an error and delivering
            # tokens that were valid
            elif self.current_char in ILLEGAL_CHARS:
                print(f'\nIllegal character "{self.current_char}" at:\nIndex {self.pos}\nLine {self.line_pos}\nColumn {self.column_pos}\n')
                return None
            else:
                print(f'\nUnrecognized token at:\nIndex {self.pos}\nLine {self.line_pos}\nColumn {self.column_pos}\n')
                return None

        return tokens
    

    # skips to next line
    def skip_line(self):
        tokens = []

        while self.current_char != None and self.current_char != '\n':
            self.advance()
            
        tokens.append(COMMENT)
        return tokens
    

# creates operation tokens, includes parentheses
    def make_operater(self):
        if self.current_char == '+':
            op_type = PLUS
            op_value = '+'
        elif self.current_char == '-':
            op_type = MINUS
            op_value = '-'
        elif self.current_char == '/':
            op_type = DIVIDE
            op_value = '/'
        elif self.current_char == '*':
            op_type = MUL
            op_value = '*'
        elif self.current_char == '(':
            op_type = OPEN_PAR
            op_value = '('
        elif self.current_char == ')':
            op_type = CLOSE_PAR
            op_value = ')'
        
        self.advance()
        return Token(op_type, op_value)


#make number function - to make numbers from user entry
    def make_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char != None and self.current_char in DIGITS + '.':

            if self.current_char == '.':
                dot_count += 1
            
            num_str += self.current_char

            self.advance()

        if dot_count == 0:
            return Token(INT, int(num_str))
        else:
            return Token(FLOAT, float(num_str))
            
        
     


# executing function
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens = lexer.make_tokens()
    return tokens
