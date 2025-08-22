import random
num = random.randint(1,10)
guess_num1 = int(input("Guess a number between 1 and 10: "))
if guess_num1 == num:
    print("Congratulations! You guessed the number.")
elif guess_num1 > 10:
    print("Sorry, you guessed a number greater than 10. Try again.")
elif guess_num1 < num:
    print("Sorry, you guessed too low. Try again.")
    guess_num2 = int(input("Guess again: "))
    if guess_num2 == num:
        print("Congratulations! You guessed the number.")
    elif guess_num2 < guess_num1:
        print("Are you stupid? Did you understand my words?.")
        print(f"As punishment,you lose the chance to guess the number. The number was{num}")
    elif guess_num2 < num and guess_num2 > guess_num1:
        print("Sorry, you guessed too low. Try again.")
    elif guess_num2 > 10:
        print("Sorry, you guessed a number greater than 10. Try again.")
        guess_num3 = int(input("Guess again, I am sorry to tell you that it's your last chance: "))
        if guess_num3 == num:
            print("Congratulations! You guessed the number.")
        elif guess_num3 < guess_num2:
            print("Are you stupid? Did you understand my words?.")
            print(f"As punishment,you can't guess the number. The number was{num}")
        elif guess_num3 < num and guess_num3 > guess_num2:
            print("Sorry, you guessed too low. Try again.")
        elif guess_num3 > 10:
            print("Sorry, you guessed a number greater than 10. Try again.")
    elif guess_num2 > num:
        print("Sorry, you guessed too high. Try again.")
        guess_num3 = int(input("Guess again, I am sorry to tell you that it's your last chance: "))
        if guess_num3 == num:
            print("Congratulations! You guessed the number.")
        elif guess_num3 > guess_num2:
            print("Are you stupid? Did you understand my words?.")
            print(f"As punishment,you can't guess the number. The number was{num}")
        elif guess_num3 > num and guess_num3 < guess_num2:
            print("Sorry, you guessed wrong. The number was", num)
        elif guess_num3 <num:
            print("Sorry, you guessed wrong. The number was", num)
        else:
            print("Sorry, you guessed wrong. The number was", num)
elif guess_num1 > num:
    print("Sorry, you guessed too high. Try again.")    
    guess_num2 = int(input("Guess again: "))
    if guess_num2 == num:
        print("Congratulations! You guessed the number.")
    elif guess_num2 > guess_num1:
        print("Are you stupid? Did you understand my words?.")
        print(f"As punishment,you lose the chance to guess the number. The number was{num}")
    elif guess_num2 < num and guess_num2 < guess_num1:
        print("Sorry, you guessed too low. Try again.")
    elif guess_num2 > num and guess_num2 < guess_num1:
        print("Sorry, you guessed too low. Try again.")
        guess_num3 = int(input("Guess again, I am sorry to tell you that it's your last chance: "))
        if guess_num3 == num:
            print("Congratulations! You guessed the number.")
        else:
            print("Sorry, you guessed wrong. The number was", num)
    
