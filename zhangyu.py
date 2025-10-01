colors = 5
count = 0
for c0 in range(1, colors+1):
    for c1 in range(1, colors+1):
            for c2 in range(1, colors+1):
                for c3 in range(1, colors+1):
                    for c4 in range(1, colors+1):
                        for c5 in range(1, colors+1):
                            for c6 in range(1, colors+1):
                                for c7 in range(1, colors+1):
                                    # 检查所有相邻顶点颜色不同
                                    if (c0 != c1 and c0 != c3 and c0 != c4 and
                                        c1 != c2 and c1 != c5 and
                                        c2 != c3 and c2 != c6 and
                                        c3 != c7 and
                                        c4 != c5 and c4 != c7 and
                                        c5 != c6 and
                                        c6 != c7):
                                        count += 1
print(count)