#定义外层循环,用while循环
i = 1
while i <= 9:
    #定义内层循环
    j = 1
    while j <= i:
        print(f"{i}x{j}={i*j}\t", end=" ")
        j += 1
    i += 1
    print()#空的print()函数用于换行

print("hello \tworld \t e")
print("hello \tpython \t s")

# 以下for代码输出九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}x{j}={i*j}\t", end=" ")
    print()

i = 1
count = 0
while i <= 10:
    j = 1
    while j <= 10:
        print(f"今天是第{i}天，送给你{j}个蛋糕")
        j += 1
        count += 1
    i += 1
print(f"一共送了{count}个蛋糕")

print("程序1结束")

i = 1
count = 0
for i in range(1, 11):
    for j in range(1, 11):
        print(f"今天是第{i}天，送给你{j}个蛋糕")
        count += 1
print(f"一共送了{count}个蛋糕")
print("程序2结束")