list = [1, 2, 3, 4, 5,6,7,8,9,10]
print(list[1])
list_sort  = []
for i in list:
    if i % 2 == 0:
        list_sort.append(i)
    else:
        continue
print(list_sort)

list = [1, 2, 3, 4, 5,6,7,8,9,10]
i=0
list_sort1 = []
while i< len(list):
    if list[i] % 2 == 0:
        list_sort1.append(list[i])
        i += 1
    else:
        i += 1
print(list_sort1)

tuple1 = (1, 2, 3, 4, 5,6,7,8,9,10)
index = tuple1.index(5)
print(index)
count = tuple1.count(5)
print(count)
count1 = len(tuple1)
print(count1)
i=0
while i< len(tuple1):
    print(tuple1[i], end=" ")
    i += 1  