import lexerProgram as lp

answer = ""

while True:
    answer = input("Please type the number to select from the following:\n\nRead input.txt (1)\nEnter input manually (2)\nRun test cases(3)\n")

    while answer != "1" and answer != "2" and answer != "3":
        print("\nSorry, that isn't an available input.")
        answer = input("Please type the number to select from the following:\n\nRead input.txt (1)\nEnter input manually (2)\nRun test cases(3)\n")


    if answer == "1":
        # reads input.txt file
        try:
            with open('Projects/Project1/input.txt', 'r') as f:
                file_text = f.read()
            result = lp.run('<stdin>', file_text)
            if result:
                print(f'\n{result}\n')
        except Exception as e:
            print(f"An error occured while reading the file:\n{e}\n")
        break

    elif answer == "2":
        # begins terminal entry tokenization
        while True:
            text = input('V@D > ')
            result = lp.run('<stdin>', text)
            if result:
                print(f'\n{result}\n')

    else:
        # runs test cases
        
        #tc1: Simple tokenization
        print("\nTest Case 1: Simple tokenization")
        print("Input: '1+2'")
        
        result = lp.run('<stdin', '1+2')
        if result:
            print(f'\n{result}\n')

        #tc2: Int & float
        print("\nTest Case 2: Integer & float")
        print("Input: '3.14+2.71'")
        
        result = lp.run('<stdin', '3.14+2.71')
        if result:
            print(f'\n{result}\n')

        #tc3: Complex tokenization
        print("\nTest Case 3: Complex tokenization")
        print("Input: '(3.14/2.71)*5+(17/1.43)'")
        
        result = lp.run('<stdin', '(3.14/2.71)*5+(17/1.43)')
        if result:
            print(f'\n{result}\n')

        #tc4: Illegal character
        print("\nTest Case 4: Illegal character")
        print("Input: '4+f'")
        
        result = lp.run('<stdin', '4+f')
        if result:
            print(f'\n{result}\n')

        #tc5: Unrecognized character
        print("\nTest Case 5: Unrecognized character")
        print("Input: '@+2'")
        
        result = lp.run('<stdin', '@+2')
        if result:
            print(f'\n{result}\n')

        #tc6: Operation followed by comment
        print("\nTest Case 6: Operation followed by comment")
        print("Input: '4/6! This is a comment'")
        
        result = lp.run('<stdin', '4/6! This is a comment')
        if result:
            print(f'\n{result}\n')

        #tc7: New line demonstrated in input.txt
        print("\nTest Case 7: New line capabilities shown with an error")
        print("Input:\n '1+2\n4+p'")
        
        result = lp.run('<stdin', '1+2\n4+p')
        if result:
            print(f'\n{result}\n')

        #tc8: New line demonstrated in input.txt
        print("\nTest Case 8: Comment in new line")
        print("Input:\n '! this function divides 4 by 3\n(4/3)'")
        
        result = lp.run('<stdin', '! this function divides 4 by 3\n(4/3)')
        if result:
            print(f'\n{result}\n')

        break
    