n = int(input("输入一个整数"))
a,b = 0,1
sum = 0
for _ in range(n):
    a,b = b,a+b
    p = 1/a 
    r = b/a
    sum += p
print()
print(sum)



    