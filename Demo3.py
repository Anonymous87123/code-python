print("礼物派送中，满足条件即可领取：")
age = int(input("Enter your age: "))
if age >= 18 and age <= 60:
    print("你是成年人了，符合年龄要求")
    if int(input("Enter your work years: ")) >= 3: 
        print("你工作经验符合要求")
        print("恭喜你获得礼物")
    else:
        print("你工作经验不足，接下来验证您的级别")    
        if int(input("Enter your working status: ")) >=3:
            print("你的级别达标，符合礼物派送要求")
        elif ValueError:
            print("输入有误，请重新输入")
        else:
            print("你还未达到领取条件")
elif age < 18:
    print("你未满18岁，不符合领取条件") 
elif age > 60:
    print("你超过60岁，不符合领取条件") 
elif ValueError:
    print("输入有误，请重新输入")

