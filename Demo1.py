height=float(input("请输入您的身高，注意单位是米:"));
weight=float(input("请输入您的体重，注意单位是千克:"));
bmi=weight/(height*height)
if bmi<18.5:
    print("您的bmi指数为:"+str(bmi))
    print("体重过轻")
if bmi>=18.5 and bmi<24.9:
    print("您的bmi指数为:"+str(bmi))
    print("体重正常")
if bmi>=24.9 and bmi<29.9:
    print("您的bmi指数为:"+str(bmi))
    print("体重稍重")
if bmi>=29.9:
    print("您的bmi指数为:"+str(bmi))
    print("体重过重")

m=313.5
n=str(m)
s=int(m)
ss=str(s)
print("商品总金额为"+n+"元")
print("实际支付金额为"+ss+"元")

x=input("请您为电影打分(只能输入0-10的整数):")
y=int(x)
print("好的，您的评分是："+"⭐"*y)

print("打折活动火热进行中...")
x=input("请用数字回答今天是星期几？你的回答是：")
y=int(input("请用数字回答现在几点了？(24小时制),你的回答是："))
if (x==2 and (y>=19 and y<=20)) or (x==3 and (y>=19 and y<=20)):
    print("恭喜你获得10%的折扣！")
else:
    print("折扣活动未开始或已结束，不享受折扣。")

name= '\'还在尬黑 %s\''%("那么你呢")
print(name)
name = "I am haizaigahei, %s"%("and you?")
print(name)
name = "I am haizaigahei%s"%(123)
print(name)
int_num = int(3.1415926)
name = "I am haizaigahei%x"%(int_num)
print(name)

name = "haizaigahei"
avg_salary = 50000
message = "I am %s, the average salary of my company is %d"%(name,avg_salary)
print(message)

name = "haizaigahei"
year = 2021
price = 3.13
message = "my name is %s,and I am %d years old, and the price is %f dollars" %(name, year, price)
print(message)

num1 = 11.345
name = "John"
message = "hello,I am %s,my favorite number is %.2f "%(name,num1)
print(message)

name = "John"
age = 25
print(f"my name is {name},and my age is {age}")

sum=1+1
print("1+1= %d"%(sum))
print(f"1+1={1+1}")
print("字符串在python中的类型是%s"%(type("字符串")))

name = "张三"
age = 25
print("我的名字是%s，今年%d岁。"%(name,age))

print(f"字符串的类型是{type('字符串')}")

time = input("填数字,如1，2，3,现在给出数字：")
time1 = int(time)
name = "宇强传媒"
stock_price = 19.99
stock_code = "000001" 
factor = 1.1
result1 = factor ** time1
result2 = stock_price*result1
print(f"{name}当前的股价为{stock_price}元")
print(f"{time}天后,{name},即股票代号{stock_code}的股价将会涨到{result2:.6}元")

if int(input("你的身高是多少厘米："))>=120:
    print("对不起，您的身高不符合免费要求。")
    print("but if you have vip, you can enjoy for free too")
    if int(input("是否有会员？（1是，0否）"))==1:
        print("恭喜您，您已获得免费特权！")
    else:
        print("抱歉，您没有会员资格。")
else:
    print("恭喜您，您的身高符合免费要求。")