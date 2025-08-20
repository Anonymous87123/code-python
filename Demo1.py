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
message = "hello，I am %s,my favorite number is %.2f "%(name,num1)
print(message)