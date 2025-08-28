def ln2():
    sum = 0
    n =2
    for i in range(n+1,2*n+1):
        div = 1/i
        sum += div
        print(sum)
        choice = input("Do you want to continue? (1): ")
        if choice == "1":
            n += 1
            sum = 0
            ln2()
ln2()