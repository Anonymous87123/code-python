# to count the number of 'e' in a string.
str = input("Enter a string: ")
count = 0
for i in str:
    if i == 'e':
        count += 1
    else:
        continue
print("The count of 'e' in the string is:", count)
