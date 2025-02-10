#Create a Tocken Class as given below
class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, '{self.value}')"

#Create TOCKENS list
VD_INT  = 'VD_INT'
VD_FLOAT = 'VD_FLOAT'
VD_PLUS  = 'VD_PLUS'
VD_MINUS = 'VD_MINUS'
VD_DIVIDE = 'VD_DIVIDE'
VD_MULT = 'VD_MULT'

#Create number list
DIGITS = '0123456789'

#Create Operators list
OPERATORS = '+-/*'

#Create a lexer class constructor as below 
class Lexer:
    def __init__(self, fn, text):
        self.fn = fn    
        self.text = text
        self.pos = -1 
        self.current_char = None
        self.advance()
        
# Complete the advance function below to move thru characters
    def advance(self): # complete the function to move to next character, and assign the character to self.current_char if not past the last character.
        
        # incrementing by 1
        self.pos += 1

        if self.pos < len(self.text):
            self.current_char=self.text[self.pos]
        else:
            self.current_char=None
            

# New token maker
    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in OPERATORS:
                tokens.append(self.make_operater())
            elif self.current_char in DIGITS: 
                tokens.append(self.make_number())
            else: pass
        return tokens
    

# new operater finder
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
            return Token(VD_INT, int(num_str))
        else:
            return Token(VD_FLOAT, float(num_str))
            
        

     
# Executing function

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens = lexer.make_tokens() 
    return tokens