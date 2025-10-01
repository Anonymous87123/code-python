def exact_probability():
    """
    计算精确概率（使用状态转移）
    """
    # 状态：已收集的偶数集合
    # 初始状态：空集，概率为1
    states = {
        frozenset(): 1.0
    } 
    # 转移概率
    p_even = 3/6  # 掷出偶数的概率
    p_odd = 3/6   # 掷出奇数的概率
    total_prob = 0.0
    # 模拟直到收敛（或达到合理深度）
    for _ in range(10000):  # 足够深的迭代
        new_states = {}
        for state, prob in states.items():
            # 如果掷出奇数，结束序列
            total_prob += prob * p_odd * (len(state) == 3)
            
            # 如果掷出偶数，更新状态
            for even_num in [2, 4, 6]:
                if even_num not in state:
                    new_state = state | {even_num}
                    new_states[new_state] = new_states.get(new_state, 0) + prob * p_even * (1/3)
        
        states = new_states
        if not states:  # 所有可能状态都已处理
            break
    print(total_prob)
    return total_prob

# 计算精确概率
exact_prob = exact_probability()



