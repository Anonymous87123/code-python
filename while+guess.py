import random
num = random.randint(1,100)
count = 0
flag = True
while flag:
    guess = int(input("Guess the number between 1 and 100: "))
    count += 1
    if guess == num:
        print(f"Congratulations!But you guessed the number eventually.")
        flag = False
    else:
        if guess > num:
            print("Sorry, the random number is smaller.Now please try again.")
        if guess < num:
            print("Sorry, the random number is larger.Now please try again.")
print(f"You have guessed {count} times")    
        

