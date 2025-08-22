money = 12000
for i in range(1,21):
    import random
    score = random.randint(1,10)
    import random
    salary = random.randint(1000,1400)
    if score <= 5:
        print(f"员工{i}的绩效是{score}，不发工资")
        continue
    if money >= 1000:
        money -= salary
        print(f"员工{i}的绩效是{score}，发放{salary}元工资，剩余{money}元")
    else:
        print(f"余额不足，还剩下{money}元，不发工资")
        break
