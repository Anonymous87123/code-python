while True:
    try:
        num = int(input("输入一个不是1的奇数: "))
        if num % 2 == 1:
            break
        elif num % 2 == 0:
            print("输入错误，请重新输入")
            continue
        elif num == 1:
            print("输入错误，请重新输入")
            continue
    except ValueError:
        print("输入错误，请重新输入")
        continue
num2 = num + 1
num1 = int(num2 / 2)
for i in range(1,num1 + 1):
    print("* "*i)
    print()
for j in range(1, num1):
    m = num1 - j
    print("* "*m)
    print()


