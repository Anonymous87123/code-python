import tkinter as tk
class SuperCalculator24:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Calculator '24' point")
        self.root.geometry("450x750")# 设置窗口大小,单位是像素,一个像素的边长约为0.22mm
        # 创建特殊字符串变量,它们与Entry小部件绑定,用于存储输入的数字,同步显示
        self.input_var1 = tk.StringVar()
        self.input_var2 = tk.StringVar()
        self.input_var3 = tk.StringVar()
        self.input_var4 = tk.StringVar()
        # 创建主框架，并设置填充、扩展、边距属性, pack()方法用于将组件放置在父组件中
        # fill=tk.BOTH表示填充父组件的整个空间，expand=True表示组件可以扩展到最大尺寸
        # padx和pady分别表示水平和垂直方向上的边距
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        # 输入框框架，Frame()方法用于创建框架，grid()方法用于将组件放置在父组件中
        # columnspan=4表示该框架占据4列，sticky='nsew'表示组件可以向四周扩展
        # padx和pady分别表示水平和垂直方向上的边距，row=0表示该框架位于第一行
        input_frame = tk.Frame(main_frame)
        input_frame.grid(row=0, column=0, columnspan=4, pady=10, sticky='nsew')      
        # 添加输入框指引标签，并设置字体、字号、边距、位置属性
        # width=15表示输入框宽度为15个字符，bd=5表示边框宽度为5个像素
        # textvariable=self.input_var1表示绑定变量self.input_var1到输入框
        # anchor='w'表示标签左对齐，font=("Arial", 14)表示字体为Arial，字号为14
        # padx和pady分别表示水平和垂直方向上的边距，sticky='e'表示标签右对齐
        # row=0表示该标签位于第一行，column=0表示该标签从第一列开始放置
        guide = "认为J,Q,K分别是11,12,13"
        tk.Label(input_frame, text=f"第1个数,{guide}:", font=("Arial", 14)).grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.display1 = tk.Entry(input_frame, textvariable=self.input_var1, font=("Arial", 18), width=15, bd=5)
        self.display1.grid(row=0, column=1, columnspan=3, pady=5, sticky='we')
        # column=1表示该标签从第二列开始放置，columnspan=3表示该标签占据3列，sticky='we'表示标签水平方向上对齐
        tk.Label(input_frame, text=f"第2个数,{guide}:", font=("Arial", 14)).grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.display2 = tk.Entry(input_frame, textvariable=self.input_var2, font=("Arial", 18), width=15, bd=5)
        self.display2.grid(row=1, column=1, columnspan=3, pady=5, sticky='we')
        # grid()方法是将组件放置在父组件中
        tk.Label(input_frame, text=f"第3个数,{guide}:", font=("Arial", 14)).grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.display3 = tk.Entry(input_frame, textvariable=self.input_var3, font=("Arial", 18), width=15, bd=5)
        self.display3.grid(row=2, column=1, columnspan=3, pady=5, sticky='we')
        tk.Label(input_frame, text=f"第4个数,{guide}:", font=("Arial", 14)).grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.display4 = tk.Entry(input_frame, textvariable=self.input_var4, font=("Arial", 18), width=15, bd=5)
        self.display4.grid(row=3, column=1, columnspan=3, pady=5, sticky='we')
        # 结果框架，Frame()方法用于创建框架，grid()方法用于将组件放置在父组件中
        # columnspan=4表示该框架占据4列，sticky='nsew'表示组件可以向四周扩展
        result_frame = tk.Frame(main_frame)
        result_frame.grid(row=1, column=0, columnspan=4, pady=10, sticky='nsew')
        result_label = tk.Label(result_frame, text="计算结果:", font=("Arial", 16))
        result_label.pack(anchor='w')# 结果标签
        # 使用Text小部件和滚动条来显示所有解法
        text_frame = tk.Frame(result_frame)
        text_frame.pack(fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(text_frame)# scrollbar()方法用于创建滚动条
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # pack()方法是将组件放置在父组件中，和grid()方法类似，但它可以自动调整组件的大小
        # fill=tk.BOTH表示填充父组件的整个空间，expand=True表示组件可以扩展到最大尺寸
        # side=tk.RIGHT表示滚动条位于右边，fill=tk.Y表示文本区域可以垂直扩展
        # 文本区域 - 设置为只读
        self.result_text = tk.Text(text_frame, height=10, width=60, font=("Arial", 12),
                                  yscrollcommand=scrollbar.set, wrap=tk.WORD, state=tk.DISABLED)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.result_text.yview)
        # config 方法用于设置滚动条的属性，command=self.result_text.yview表示绑定滚动条的滚动动作到文本区域
        # wrap=tk.WORD表示文本自动换行，state=tk.DISABLED表示文本区域不可编辑
        # height=10表示文本区域高度为10行，width=60表示文本区域宽度为60个字符
        # yscrollcommand=scrollbar.set表示绑定滚动条的滚动动作到文本区域
        self.input_vars = [self.input_var1, self.input_var2, self.input_var3, self.input_var4]
        self.displays = [self.display1, self.display2, self.display3, self.display4]
        # 按钮框架，按钮框架本身没有设置固定大小，而是由内部按钮的大小和间距决定。按钮框架会根据内容自动调整大小。
        # 网格自动居中，因为左右两侧有相等的空白空间
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=4, pady=10)
        self.create_buttons(button_frame)
        # 配置权重,括号里的1表示权重为1，表示该组件占据整个父组件的空间
        main_frame.grid_rowconfigure(1, weight=1)
        for i in range(4):
            main_frame.grid_columnconfigure(i, weight=1)
    def create_buttons(self, parent):
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('0', 3, 0)  # 将0按钮放在第3行第0列
        ]
        for (text, row, col) in buttons:
            button = tk.Button(parent, text=text, font=("Arial", 18), 
                              height=1, width=3, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5) 
        start_button = tk.Button(
            parent, text="开始计算", font=("Arial", 16),
            height=1, width=10, command=lambda: self.button_click("开始计算")
        )
        start_button.grid(row=4, column=0, columnspan=3, pady=10)  
        clear_button = tk.Button(
            parent, text="清除", font=("Arial", 16),
            height=1, width=10, command=self.clear_all
        )
        clear_button.grid(row=5, column=0, columnspan=3, pady=5)
    def clear_all(self):
        for var in self.input_vars:
            var.set("")
        # 清除结果文本区域时，需要先启用再禁用
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)
    def button_click(self, text):
        if text == "开始计算":
            num_list = []
            try:
                for var in self.input_vars:
                    value = var.get()
                    if value:# if value这种写法是一种简写形式，等价于if value!= ""
                        num_list.append(int(value))
                if len(num_list) != 4:
                    # 更新结果文本区域时，需要先启用再禁用，config()方法用于设置组件的属性
                    # delete()方法用于删除文本区域中的内容，insert()方法用于插入文本
                    # 1.0表示从第一行开始，tk.END表示从最后一行结束
                    # tk.disabled表示文本区域不可编辑
                    self.result_text.config(state=tk.NORMAL)
                    self.result_text.delete(1.0, tk.END)#删除文本区域中的从头到尾的内容
                    self.result_text.insert(tk.END, "请输入4个数字!")
                    self.result_text.config(state=tk.DISABLED)
                    return
                results = self.calculate(num_list)
                self.result_text.config(state=tk.NORMAL)
                self.result_text.delete(1.0, tk.END)
                if results: #是简写，意思是若results存在，则执行下面的语句，否则不执行
                    counter = 1
                    for result in results:
                        nums, ops, pattern = result #解包元组，分别取出nums、ops、pattern
                        # 根据运算顺序直接翻译下文的解法，expression是表达式的意思
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
                        # 检查是否已经存在相同的排列
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
                    pass    #pass关键字用于忽略异常
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