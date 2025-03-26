
#Create TOCKENS list
VD_PLUS  = 'VD_PLUS'
VD_MINUS = 'VD_MINUS'
VD_DIVIDE = 'VD_DIVIDE'
VD_MULT = 'VD_MULT'

# create illegal characters
ILLEGAL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Create number list
DIGITS = '0123456789'

#Create Operators list
OPERATORS = '+-/*()'

#Create a Tocken Class as given below
class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, '{self.value}')"

#Create a parser class constructor as below
class Parser:
    def __init__(self, text):
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
            
        return tokens
    

# creates operation tokens, includes parentheses
    def make_operater(self):
        tokens = []
        while self.current_char != None and self.current_char in OPERATORS + '.':

            if self.current_char == '+':
                tokens.append(VD_PLUS)
            elif self.current_char == '-':
                tokens.append(VD_MINUS)
            elif self.current_char == '/':
                tokens.append(VD_DIVIDE)
            elif self.current_char == '*':
                tokens.append(VD_MULT)
            elif self.current_char == '(':
                tokens.append("(")
            elif self.current_char == ')':
                tokens.append(")")
            self.advance()
        return tokens


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
            return Token(num_str)
        else:
            return Token(num_str)
            
    

# executing function
def run(text):
    parser = Parser(text)
    tokens = parser.make_tokens()
    return tokens

run("1 + 2 * 3")
