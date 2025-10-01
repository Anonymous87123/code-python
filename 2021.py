from itertools import permutations
list0 = [2, 0, 2, 4, 20, 24]
unique_numbers = set()
# 生成所有可能的排列
for perm in permutations(list0):
    # 将排列转换为字符串列表
    num_str = ''.join(map(str, perm))
    # 检查是否满足8位数且首位不为0
    if len(num_str) == 8 and num_str[0] != '0':
        unique_numbers.add(num_str)
print(len(unique_numbers))
