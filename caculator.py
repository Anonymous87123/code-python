def caculator():
    flag = True
    while flag:
        try:
            num1 = float(input("Enter first number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        function1 = str(input("choose'+'or'-'or'*'or'/': "))
        if function1 != '+' and function1!= '-' and function1!= '*' and function1!= '/':
            print("Invalid input! Please enter a valid operator.")
            continue
        else:
            try:
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue
            if function1 == '+':
                result = num1 + num2
            elif function1 == '-':
                result = num1 - num2
            elif function1 == '*':
                result = num1 * num2
            elif function1 == '/':
                result = num1 / num2
            choose = input("press'='to see the result,or choose'+,-,*,/'to continue: ")
            if choose =="=":
                print(result)
                flag = False
            else:
                caculator()
caculator()     

