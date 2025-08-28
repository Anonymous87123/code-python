money = 10000
def check():
    print("您的余额为:",money,"元")
def deposit():
    global money
    while True:
        try:
            global money
            money += float(input("请输入存款金额:"))
            print(f"存款成功,余额为{money}元")
            break
        except ValueError:
            continue
def withdraw():
    global money
    while True:
        try:
            withdraw_money = float(input("请输入取款金额:"))
            money -= withdraw_money
            if money < 0:
                print("取款失败,余额不足")
                money += withdraw_money
                continue
            else:
                print("取款成功,余额为",money,"元")
                break
        except ValueError:
            print("请重新输入数字，额度大于10000时无法取钱")
            continue
def mian():
    print("欢迎来到ATM机")
    while True:
        try:
            card = int(input("请插卡,扣1表示已经插入,扣2表示退出ATM机:"))
            if card == 1:
                print("请选择业务:")
                print("1.查询余额")
                print("2.存款")
                print("3.取款")
                while True:
                    try:
                        choice = int(input("请输入您的选择1或2或3:"))  # 选择业务
                        if choice == 1:
                            check()
                            mian()
                        elif choice == 2:
                            deposit()
                            mian()
                        elif choice == 3:
                            withdraw()
                            mian()
                        else:
                            print("请重新输入")
                            continue
                    except ValueError:
                        print("请重新输入")
                        continue
            elif card == 2:
                while True:
                    try:
                        choose = int(input("是否确认退出ATM机?1.确认退出 2.取消退出:"))
                        if choose == 1:
                            print("感谢您的使用")
                            exit()
                        elif choose == 2:
                            mian()
                        else:
                            print("请重新输入")
                            continue
                    except ValueError:
                        print("请重新输入")
                        continue
            else:
                print("请重新输入")
                mian()
        except ValueError:
            print("请重新输入")
            continue
        break    
mian()





