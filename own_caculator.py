print("Welcome to calculator!")
# 初始输入第一个数字
while True:
    try:
        result = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
# 定义函数进行运算
def perform_operation(current_result):
    while True:
        operator = input("Please choose '+' or '-' or '*' or '/': ")
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator! Please choose again.")
            continue
        break
    while True:
        try:
            num = float(input("Enter another number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    if operator == '+':
        return current_result + num
    elif operator == '-':
        return current_result - num
    elif operator == '*':
        return current_result * num
    elif operator == '/':
        if num == 0:
            print("Error: Division by zero!")
            return current_result
        return current_result / num

while True:
    choice = input("Press [=] to get result or [Enter] to continue: ")
    if choice == '=':
        print("Result:", result)
        break
    elif choice == '':
        result = perform_operation(result)
    else:
        print("Invalid input! Please press [=] or [Enter].")