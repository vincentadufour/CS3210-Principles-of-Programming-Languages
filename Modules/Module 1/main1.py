import myLexerOld #[ Use the filename of your lexer program]

while True:
    text = input('V@D > ') #Give your own prompt name here
    result = myLexerOld.run('<stdin>', text) #This should be myProgram.run
    print(result)
