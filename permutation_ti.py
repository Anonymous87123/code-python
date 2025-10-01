from itertools import permutations

# 使用更高效的方法生成所有排列
mylist = list(permutations(range(6)))  # 0-5代表6个位置

count = 0
for arrangement in mylist:
    # 解包：arrangement是6个位置的排列，索引0-5对应A-F的位置
    pos_A, pos_B, pos_C, pos_D, pos_E, pos_F = arrangement
    
    # 条件①：A和B必须相邻（顺序可互换）
    if abs(pos_A - pos_B) != 1:
        continue
    
    # 条件②：C不能站在第3位和第5位（注意：我们的位置编号是0-5，对应实际位置1-6）
    # 所以第3位对应索引2，第5位对应索引4
    if pos_C == 2 or pos_C == 4:  # 索引2=第3位，索引4=第5位
        continue
    
    # 条件③：D和E不能相邻
    if abs(pos_D - pos_E) == 1:
        continue
    
    count += 1

print(f"共有 {count} 种不同的排队方式")
