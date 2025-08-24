#长度函数
name = str(input("Enter your name: "))
lenth = len(name)
print(lenth)
#用for循环代替长度函数
count = 0
for i in str(name):
    count += 1
print(count)

str1 = str(input("Enter a string: "))
str2 = str(input("Enter another string: "))
str3 = str(input("Enter a third string: "))
def my_len(data):
    count_str = 0
    for i in data:
        count_str += 1
    print("Length of the data is:", count_str)
my_len(str1)
my_len(str2)
my_len(str3)


def check(data):
    if len(data) > 5:
        print(f"Name '{data}' is too long")
    else:
        print(f"Name:'{data}' is ok")
check(str1)
check(str2)
check(str3)

def check_score():
    while True:
        score_int = input("Enter your score: ")
        try:
            score = int(score_int)
            if score < 60:
                print(f"your score is {score}, you are failing")
                break
            elif score < 70:
                print(f"your score is {score}, you are passing")
                break
            elif score < 80:
                print(f"your score is {score}, you are good")
                break
            elif score < 90:
                print(f"your score is {score}, you are very good")
                break
            else:
                print(f"your score is {score}, you are perfect")
                break
        except ValueError:
            print("error, please enter a valid score.Please enter a number between 0 and 100")
check_score()

# 定义一个函数，计算两个数的和
def add():
    while True:
        num_input1 = input("Enter first number: ")
        num_input2 = input("Enter second number: ")
        try:
            num1 = float(num_input1)
            num2 = float(num_input2)
            add = num1 + num2
            print(f"{num1}+{num2}={add}")
            break
        except ValueError:
            print("error, please enter a valid number")
add()

# 定义一个函数，计算两个数的和，并且反馈输入问题
def sum():
    while True:
        num_input3 = input("Enter first number: ")
        try:
            num3 = float(num_input3)
        except ValueError:
            print("first number error, please enter a valid number")
            continue
        #这个continue的含义是如果try中的语句出错，则直接跳过后面的语句，重新执行while循环
        #想像一下，你打篮球完了之后就吃饭，然后没投中，这个时候你就得“继续”打，而不是直接结束程序
        num_input4 = input("Enter second number: ")
        try:
            num4 = float(num_input4)
        except ValueError:
            print("second number error, please enter a valid number")
            continue
        add = num3 + num4
        print(f"{num3}+{num4}={add}")
        break#这个break的含义是，如果try中的语句没有出错，则直接跳出while循环，结束函数的执行
sum()

    