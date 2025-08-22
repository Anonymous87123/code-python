#定义外层循环
i = 1
while i <= 9:
    #定义内层循环
    j = 1
    while j <= i:
        print(f"{i}x{j}={i*j}\t", end=" ")
        j += 1
    i += 1
    print()#空的print()函数用于换行
