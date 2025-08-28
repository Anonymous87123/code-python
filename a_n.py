import msvcrt
def again():
    flag = True
    n =10000
    sum = 0
    while flag:
        m = n+1
        u = n*2+1
        sum = 0
        for i in range(m,u):
            calc = 1/i
            sum += calc
        print(sum)
        sum1 = sum + 0.25/(m-1)
        print(sum1)
        choose = input("按下回车继续")
        if choose == '':
            n += 1
            flag = True
        else:
            break
again() 

