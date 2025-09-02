def calculate_step(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return float("inf")
        return a / b
    else:
        return float("inf")

def generate_permutations(numbers_list):
    if len(numbers_list) != 4:
        raise ValueError("List should have 4 elements")
    permutations = []
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list)):
            if i == j:
                continue
            for k in range(len(numbers_list)):
                if i == k or j == k:
                    continue
                for l in range(len(numbers_list)):
                    if i == l or j == l or k == l:
                        continue
                    permutation = [numbers_list[i], numbers_list[j], numbers_list[k], numbers_list[l]]
                    if permutation not in permutations:
                        permutations.append(permutation)
    return permutations

def calculate24(numbers_list):
    if len(numbers_list) != 4:
        raise ValueError("List should have 4 elements")
    operators = ["+", "-", "*", "/"]
    operators_permutations = []
    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                operators_permutations.append([op1, op2, op3])
    
    results = []
    permutations = generate_permutations(numbers_list)
    
    for perm in permutations:
        for op in operators_permutations:
            # 1. ((a op b) op c) op d
            try:
                result = calculate_step(perm[0], perm[1], op[0])
                result = calculate_step(result, perm[2], op[1])
                result = calculate_step(result, perm[3], op[2])
                if abs(result - 24) < 0.000001:
                    results.append((perm.copy(), op.copy(), "((a op b) op c) op d"))
            except:
                pass
            
            # 2. (a op (b op c)) op d
            try:
                inner = calculate_step(perm[1], perm[2], op[1])  # 先计算b和c
                result = calculate_step(perm[0], inner, op[0])   # 然后a和上面的结果
                result = calculate_step(result, perm[3], op[2])  # 最后和d计算
                if abs(result - 24) < 0.000001:
                    results.append((perm.copy(), op.copy(), "(a op (b op c)) op d"))
            except:
                pass
            
            # 3. a op (b op (c op d))
            try:
                inner = calculate_step(perm[2], perm[3], op[2])  # 先计算c和d
                result = calculate_step(perm[1], inner, op[1])   # 然后b和上面的结果
                result = calculate_step(perm[0], result, op[0])  # 最后a和上面的结果
                if abs(result - 24) < 0.000001:
                    results.append((perm.copy(), op.copy(), "a op (b op (c op d))"))
            except:
                pass
            
            # 4. a op ((b op c) op d)
            try:
                inner = calculate_step(perm[1], perm[2], op[1])  # 先计算b和c
                result = calculate_step(inner, perm[3], op[2])   # 然后上面的结果和d
                result = calculate_step(perm[0], result, op[0])  # 最后a和上面的结果
                if abs(result - 24) < 0.000001:
                    results.append((perm.copy(), op.copy(), "a op ((b op c) op d)"))
            except:
                pass
            
            # 5. (a op b) op (c op d)
            try:
                left = calculate_step(perm[0], perm[1], op[0])   # 先计算a和b
                right = calculate_step(perm[2], perm[3], op[2])  # 同时计算c和d
                result = calculate_step(left, right, op[1])      # 最后两个结果计算
                if abs(result - 24) < 0.000001:
                    results.append((perm.copy(), op.copy(), "(a op b) op (c op d)"))
            except:
                pass
    
    return results

def main():
    numbers_list = []
    num1 = int(input("Enter the first number between 1 and 10: "))
    num2 = int(input("Enter the second number between 1 and 10: "))
    num3 = int(input("Enter the third number between 1 and 10: "))
    num4 = int(input("Enter the fourth number between 1 and 10: "))
    numbers_list.append(num1)
    numbers_list.append(num2)
    numbers_list.append(num3)
    numbers_list.append(num4)
    
    results = calculate24(numbers_list)
    
    if len(results) == 0:
        print("No solution found")
    else:
        print("Solution(s) found:")
        for i, (perm, ops, method) in enumerate(results, 1):
            # 格式化输出表达式
            expression = f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]}"
            print(f"{i}. {expression} = 24 ({method})")

if __name__ == "__main__":
    main()
            




    