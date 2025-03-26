#Create number list
DIGITS = '0123456789'

#Create Operators list
OPERATORS = '+-/*()'



def makeOperator(op):
    if op == "+":
        return "PLUS"
    elif op == "-":
        return "MINUS"
    elif op == "*":
        return "MULT"
    elif op == "/":
        return "DIV"
    else:
        return "Unrecognized operator."
    
# def makeParentheses(string):




def bincn(string):
    arr = []

    # add spaces between each char
    spacedString = " ".join(string)

    spacedString = spacedString.split()

    for i in spacedString:
        if i in OPERATORS:
            makeOperator(i)
        elif i in DIGITS:
            arr.append(i)


bincn("1 + 2 * 3")
