import tkinter as tk
import datetime
import json
import os

class SuperCalculator24:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Calculator '24' point")
        self.root.geometry("500x800")  # 增加窗口宽度
        self.root.configure(bg="#f0f0f0")
        
        # 创建历史记录文件
        self.history_file = "calculator_history.json"
        self.history = self.load_history()
        
        # 创建特殊字符串变量
        self.input_var1 = tk.StringVar()
        self.input_var2 = tk.StringVar()
        self.input_var3 = tk.StringVar()
        self.input_var4 = tk.StringVar()
        
        # 创建主框架
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # 输入框框架
        input_frame = tk.Frame(main_frame, bg="#f0f0f0")
        input_frame.grid(row=0, column=0, columnspan=4, pady=10, sticky='nsew')      
        
        # 添加输入框指引标签
        guide = "认为J,Q,K分别是11,12,13"
        tk.Label(input_frame, text=f"第1个数,{guide}:", font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.display1 = tk.Entry(input_frame, textvariable=self.input_var1, font=("Arial", 18), width=15, bd=3, relief=tk.SUNKEN)
        self.display1.grid(row=0, column=1, columnspan=3, pady=5, sticky='we')
        
        tk.Label(input_frame, text=f"第2个数,{guide}:", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.display2 = tk.Entry(input_frame, textvariable=self.input_var2, font=("Arial", 18), width=15, bd=3, relief=tk.SUNKEN)
        self.display2.grid(row=1, column=1, columnspan=3, pady=5, sticky='we')
        
        tk.Label(input_frame, text=f"第3个数,{guide}:", font=("Arial", 14), bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.display3 = tk.Entry(input_frame, textvariable=self.input_var3, font=("Arial", 18), width=15, bd=3, relief=tk.SUNKEN)
        self.display3.grid(row=2, column=1, columnspan=3, pady=5, sticky='we')
        
        tk.Label(input_frame, text=f"第4个数,{guide}:", font=("Arial", 14), bg="#f0f0f0").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.display4 = tk.Entry(input_frame, textvariable=self.input_var4, font=("Arial", 18), width=15, bd=3, relief=tk.SUNKEN)
        self.display4.grid(row=3, column=1, columnspan=3, pady=5, sticky='we')
        
        # 结果框架
        result_frame = tk.Frame(main_frame, bg="#f0f0f0")
        result_frame.grid(row=1, column=0, columnspan=4, pady=10, sticky='nsew')
        result_label = tk.Label(result_frame, text="计算结果:", font=("Arial", 16), bg="#f0f0f0")
        result_label.pack(anchor='w')
        
        # 使用Text小部件和滚动条来显示所有解法
        text_frame = tk.Frame(result_frame, bg="#f0f0f0")
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建水平和垂直滚动条
        v_scrollbar = tk.Scrollbar(text_frame)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        h_scrollbar = tk.Scrollbar(text_frame, orient=tk.HORIZONTAL)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # 文本区域 - 增加宽度并添加水平滚动条
        self.result_text = tk.Text(
            text_frame, 
            height=10, 
            width=80,  # 增加宽度到80个字符
            font=("Arial", 12),
            wrap=tk.NONE,  # 不自动换行，允许水平滚动
            xscrollcommand=h_scrollbar.set,
            yscrollcommand=v_scrollbar.set,
            state=tk.DISABLED,
            bd=2, 
            relief=tk.SUNKEN, 
            bg="white"
        )
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 配置滚动条
        v_scrollbar.config(command=self.result_text.yview)
        h_scrollbar.config(command=self.result_text.xview)
        
        self.input_vars = [self.input_var1, self.input_var2, self.input_var3, self.input_var4]
        self.displays = [self.display1, self.display2, self.display3, self.display4]
        
        # 按钮框架
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.grid(row=2, column=0, columnspan=4, pady=10)
        self.create_buttons(button_frame)
        
        # 配置权重
        main_frame.grid_rowconfigure(1, weight=1)
        for i in range(4):
            main_frame.grid_columnconfigure(i, weight=1)
    
    def create_button(self, parent, text, row, col, command, bg="#e0e0e0", fg="black", width=3, height=1):
        """创建具有立体效果的按钮"""
        button = tk.Button(
            parent, 
            text=text, 
            font=("Arial", 18),
            bg=bg,
            fg=fg,
            bd=3,
            relief=tk.RAISED,
            activebackground="#d0d0d0",
            activeforeground=fg,
            width=width,
            height=height,
            command=command
        )
        button.grid(row=row, column=col, padx=5, pady=5)
        return button
    
    def create_buttons(self, parent):
        # 数字按钮颜色
        num_bg = "#e0e0e0"
        num_fg = "black"
        
        # 功能按钮颜色
        func_bg = "#d0d0ff"
        func_fg = "black"
        
        # 历史记录按钮颜色
        history_bg = "#ffd0d0"
        history_fg = "black"
        
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('0', 3, 0)
        ]
        
        for (text, row, col) in buttons:
            self.create_button(
                parent, text, row, col, 
                command=lambda t=text: self.button_click(t),
                bg=num_bg, fg=num_fg
            )
        
        # 开始计算按钮
        self.create_button(
            parent, "开始计算", 4, 0, 
            command=lambda: self.button_click("开始计算"),
            bg=func_bg, fg=func_fg, width=10
        ).grid(columnspan=3, pady=10)
        
        # 清除按钮
        self.create_button(
            parent, "清除", 5, 0, 
            command=self.clear_all,
            bg=func_bg, fg=func_fg, width=10
        ).grid(columnspan=3, pady=5)
        
        # 历史记录按钮
        self.create_button(
            parent, "历史记录", 6, 0, 
            command=self.show_history,
            bg=history_bg, fg=history_fg, width=10
        ).grid(columnspan=3, pady=5)
    
    def load_history(self):
        """加载历史记录"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_history(self):
        """保存历史记录"""
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def add_to_history(self, numbers, solutions):
        """添加记录到历史"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "numbers": numbers,
            "solutions": solutions
        }
        self.history.append(entry)
        self.save_history()
    
    def show_history(self):
        """显示历史记录窗口"""
        history_window = tk.Toplevel(self.root)
        history_window.title("计算历史记录")
        history_window.geometry("800x600")  # 增加历史记录窗口尺寸
        history_window.configure(bg="#f0f0f0")
        
        # 标题
        tk.Label(history_window, text="历史记录", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
        
        # 历史记录框架
        history_frame = tk.Frame(history_window, bg="#f0f0f0")
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 滚动条
        v_scrollbar = tk.Scrollbar(history_frame)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        h_scrollbar = tk.Scrollbar(history_frame, orient=tk.HORIZONTAL)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # 历史记录文本区域 - 增加宽度
        history_text = tk.Text(
            history_frame, 
            height=20, 
            width=90,  # 增加宽度
            font=("Arial", 12),
            wrap=tk.NONE,  # 不自动换行，允许水平滚动
            xscrollcommand=h_scrollbar.set,
            yscrollcommand=v_scrollbar.set,
            state=tk.NORMAL,
            bd=2,
            relief=tk.SUNKEN,
            bg="white"
        )
        history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 配置滚动条
        v_scrollbar.config(command=history_text.yview)
        h_scrollbar.config(command=history_text.xview)
        
        # 显示历史记录
        if not self.history:
            history_text.insert(tk.END, "暂无历史记录")
        else:
            for i, entry in enumerate(reversed(self.history), 1):
                history_text.insert(tk.END, f"记录 {i}: {entry['timestamp']}\n")
                history_text.insert(tk.END, f"输入数字: {entry['numbers']}\n")
                history_text.insert(tk.END, f"解法 ({len(entry['solutions'])}种):\n")
                
                for j, solution in enumerate(entry['solutions'], 1):
                    expression = self.format_solution(solution)
                    history_text.insert(tk.END, f"  {j}. {expression} = 24\n")
                
                history_text.insert(tk.END, "-" * 100 + "\n\n")  # 增加分隔线长度
        
        history_text.config(state=tk.DISABLED)
        
        # 清除历史按钮
        clear_button = tk.Button(
            history_window, 
            text="清除历史记录", 
            font=("Arial", 14),
            command=lambda: self.clear_history(history_window),
            bg="#ff9999",
            bd=2,
            relief=tk.RAISED
        )
        clear_button.pack(pady=10)
    
    def format_solution(self, solution):
        """格式化解法为可读字符串"""
        nums, ops, pattern = solution
        if pattern == "((a op b) op c) op d":
            return f"(({nums[0]} {ops[0]} {nums[1]}) {ops[1]} {nums[2]}) {ops[2]} {nums[3]}"
        elif pattern == "(a op (b op c)) op d":
            return f"({nums[0]} {ops[0]} ({nums[1]} {ops[1]} {nums[2]})) {ops[2]} {nums[3]}"
        elif pattern == "a op (b op (c op d))":
            return f"{nums[0]} {ops[0]} ({nums[1]} {ops[1]} ({nums[2]} {ops[2]} {nums[3]}))"
        elif pattern == "a op ((b op c) op d)":
            return f"{nums[0]} {ops[0]} (({nums[1]} {ops[1]} {nums[2]}) {ops[2]} {nums[3]})"
        elif pattern == "(a op b) op (c op d)":
            return f"({nums[0]} {ops[0]} {nums[1]}) {ops[1]} ({nums[2]} {ops[2]} {nums[3]})"
        else:
            return "未知模式"
    
    def clear_history(self, window):
        """清除历史记录"""
        self.history = []
        self.save_history()
        window.destroy()
        self.show_history()  # 重新打开历史记录窗口
    
    def clear_all(self):
        for var in self.input_vars:
            var.set("")
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)
    
    def button_click(self, text):
        if text == "开始计算":
            num_list = []
            try:
                for var in self.input_vars:
                    value = var.get()
                    if value:
                        num_list.append(int(value))
                if len(num_list) != 4:
                    self.result_text.config(state=tk.NORMAL)
                    self.result_text.delete(1.0, tk.END)
                    self.result_text.insert(tk.END, "请输入4个数字!")
                    self.result_text.config(state=tk.DISABLED)
                    return
                results = self.calculate(num_list)
                self.result_text.config(state=tk.NORMAL)
                self.result_text.delete(1.0, tk.END)
                if results:
                    # 添加到历史记录
                    self.add_to_history(num_list, results)
                    
                    # 显示解法
                    counter = 1
                    for result in results:
                        nums, ops, pattern = result
                        if pattern == "((a op b) op c) op d":
                            expression = f"(({nums[0]} {ops[0]} {nums[1]}) {ops[1]} {nums[2]}) {ops[2]} {nums[3]}"
                        elif pattern == "(a op (b op c)) op d":
                            expression = f"({nums[0]} {ops[0]} ({nums[1]} {ops[1]} {nums[2]})) {ops[2]} {nums[3]}"
                        elif pattern == "a op (b op (c op d))":
                            expression = f"{nums[0]} {ops[0]} ({nums[1]} {ops[1]} ({nums[2]} {ops[2]} {nums[3]}))"
                        elif pattern == "a op ((b op c) op d)":
                            expression = f"{nums[0]} {ops[0]} (({nums[1]} {ops[1]} {nums[2]}) {ops[2]} {nums[3]})"
                        elif pattern == "(a op b) op (c op d)":
                            expression = f"({nums[0]} {ops[0]} {nums[1]}) {ops[1]} ({nums[2]} {ops[2]} {nums[3]})"
                        else:
                            expression = "未知模式"
                        self.result_text.insert(tk.END, f"{counter}. {expression} = 24\n")
                        counter += 1
                    self.result_text.insert(tk.END, f"\n共找到 {len(results)} 种解法")
                else:
                    self.result_text.insert(tk.END, "抱歉，没有找到解法，请换一道题吧!")
                self.result_text.config(state=tk.DISABLED)
            except ValueError:
                self.result_text.config(state=tk.NORMAL)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, "输入有误，请重新输入!")
                self.result_text.config(state=tk.DISABLED)
        else:
            focused = self.root.focus_get()
            if focused in self.displays:
                focused.insert(tk.END, text)
    
    def generate_permutations(self, num_list):
        permutations = []
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                for k in range(4):
                    if k == i or k == j:
                        continue
                    for l in range(4):
                        if l == i or l == j or l == k:
                            continue
                        permutation = [num_list[i], num_list[j], num_list[k], num_list[l]]
                        found = False
                        for p in permutations:
                            if p[0] == permutation[0] and p[1] == permutation[1] and p[2] == permutation[2] and p[3] == permutation[3]:
                                found = True
                                break
                        if not found:
                            permutations.append(permutation)
        return permutations
    
    def calculate_step(self, a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError
            return a / b
    
    def calculate(self, num_list):
        operators = ["+", "-", "*", "/"]
        operators_permutations = []
        for op1 in operators:
            for op2 in operators:
                for op3 in operators:
                    operators_permutations.append([op1, op2, op3])
        results = []
        num_permutations = self.generate_permutations(num_list)
        for nums in num_permutations:
            for ops in operators_permutations:
                # 尝试五种不同的运算顺序
                try:
                    # ((a op b) op c) op d
                    result1 = self.calculate_step(nums[0], nums[1], ops[0])
                    result2 = self.calculate_step(result1, nums[2], ops[1])
                    result = self.calculate_step(result2, nums[3], ops[2])
                    if abs(result - 24) < 0.000001:
                        results.append((nums, ops, "((a op b) op c) op d"))
                        continue
                except:
                    pass
                try:
                    # (a op (b op c)) op d
                    result1 = self.calculate_step(nums[1], nums[2], ops[1])
                    result2 = self.calculate_step(nums[0], result1, ops[0])
                    result = self.calculate_step(result2, nums[3], ops[2])
                    if abs(result - 24) < 0.000001:
                        results.append((nums, ops, "(a op (b op c)) op d"))
                        continue
                except:
                    pass
                try:
                    # a op (b op (c op d))
                    result1 = self.calculate_step(nums[2], nums[3], ops[2])
                    result2 = self.calculate_step(nums[1], result1, ops[1])
                    result = self.calculate_step(nums[0], result2, ops[0])
                    if abs(result - 24) < 0.000001:
                        results.append((nums, ops, "a op (b op (c op d))"))
                        continue
                except:
                    pass
                try:
                    # a op ((b op c) op d)
                    result1 = self.calculate_step(nums[1], nums[2], ops[1])
                    result2 = self.calculate_step(result1, nums[3], ops[2])
                    result = self.calculate_step(nums[0], result2, ops[0])
                    if abs(result - 24) < 0.000001:
                        results.append((nums, ops, "a op ((b op c) op d)"))
                        continue
                except:
                    pass
                try:
                    # (a op b) op (c op d)
                    result1 = self.calculate_step(nums[0], nums[1], ops[0])
                    result2 = self.calculate_step(nums[2], nums[3], ops[2])
                    result = self.calculate_step(result1, result2, ops[1])
                    if abs(result - 24) < 0.000001:
                        results.append((nums, ops, "(a op b) op (c op d)"))
                except:
                    pass
        return results

if __name__ == '__main__':
    root = tk.Tk()
    app = SuperCalculator24(root)
    root.mainloop()