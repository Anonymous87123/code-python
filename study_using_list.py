list1 = [1, 2, 3, 4, 5,1]
#下面演示列表的方法
#查找元素的索引
index_1= list1.index(1)#返回列表中第一个1的索引
print(index_1)

index_2= list1.index(2, 1)#返回列表中从索引2开始的第一个1的索引
print(index_2)

count_1= list1.count(1)#返回列表中1的个数
print(count_1)

#修改列表元素
list1[0] = 100
print(list1)

#在指定位置插入元素
list1.insert(2, 200)
print(list1)

#尾部添加元素
list1.append(300)
print(list1)

#在列表尾部添加多个元素
list1.extend([400, 500])
print(list1)

#删除列表末尾元素
list1.pop(1)
print(list1)
print(list1.pop(1))

#删除元素（第一个匹配的元素）
list1.remove(1)
print(list1)

#用del语句删除元素
del list1[0]
print(list1)

#清空列表
list1.clear()
print(list1)

#统计列表元素个数
print(len(list1))

#统计元素出现的次数
print(list1.count(100))

#用while循环遍历列表
i = 0
while i < len(list1):
    print(list1[i],end=' ')
    i += 1

#用for循环遍历列表
for item in list1:
    print(item,end=' ')

