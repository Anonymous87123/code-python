print("Welcome to calculator!")
result = 0 #初始化结果
while True:
    try:
        result = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue
def calculate(current_result):
    while True:
        try:
            choose = str(input("please choose '+'or'-'or'*'or'/': "))
            if choose in ['+', '-', '*', '/']:
                break
            elif choose not in ['+', '-', '*', '/']:
                print("Invalid input! Please enter a valid operator.")
                continue
        except ValueError:
            print("Error! Please check your input and try again.")
            continue
    while True:
        try:
            second_num = float(input("Enter another number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    if choose == '+':
        return current_result + second_num
    elif choose == '-':
        return current_result - second_num
    elif choose == '*':
        return current_result * second_num
    elif choose == '/':
        if second_num == 0:
            print("Error! Cannot divide by zero.")
            return current_result
        return current_result / second_num
def ask():
    global result
    while True:
        try:
            choice = str(input("press[=]to get result \nor press [Enter] to continue."))
            if choice == "=":
                print("Result: ", result)
                break
            elif choice == "":
                result = calculate(result)
        except ValueError:
            print("Error! Please check your input and try again.")
            continue
result = calculate(result)
ask()