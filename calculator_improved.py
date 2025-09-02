import tkinter as tk
from math import sqrt

class Calculator:
    def __init__(self, master):
        self.master = master
        self.result_var = tk.StringVar()
        self.master.title("Super Calculator")
        
        # 设置窗口大小和居中
        self.master.geometry("500x600")  # 增加窗口尺寸
        self.center_window()
        
        # 创建显示区域 - 增加字体大小和宽度
        self.display = tk.Entry(master, textvariable=self.result_var, 
                               font=("Arial", 28),  # 增大字体
                               insertwidth=4, width=15,  # 减少宽度显示字符数
                               borderwidth=10, justify="right")  # 右对齐
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        
        self.create_buttons()
    
    def center_window(self):
        """将窗口居中显示在屏幕上"""
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self.master.geometry(f"+{x}+{y}")
    
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('√', 5, 0), ('^2', 5, 1), ('C', 5, 2), ('求整', 5, 3),
        ]
        
        # 创建按钮 - 减少内边距
        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, 
                              font=("Arial", 16),  # 增大按钮字体
                              padx=15, pady=15,  # 减少内边距
                              width=3, height=1,  # 调整大小
                              command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)  # 增加按钮间距
        
        # 创建跨列的"求余"按钮 - 增加高度
        remainder_button = tk.Button(
            self.master, 
            text='求余', 
            font=("Arial", 16),
            padx=15, 
            pady=15, 
            width=3, 
            height=1,
            command=lambda: self.on_button_click('求余')
        )
        remainder_button.grid(row=6, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)
        
        # 配置网格行列权重 - 增加行高权重
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1)
    
    # 自定义计算函数（避免使用eval）
    def calculate(self, a, b, operator):
        """执行基本四则运算"""
        try:
            a = float(a)
            b = float(b)
            
            if operator == "+":
                return a + b
            elif operator == "-":
                return a - b
            elif operator == "*":
                return a * b
            elif operator == "/":
                if b == 0:
                    return "Error: Division by zero"
                return a / b
            else:
                return "Error: Invalid operator"
        except ValueError:
            return "Error: Invalid number"
    
    def calculate_square(self, num):
        """计算平方"""
        try:
            num = float(num)
            return num * num
        except ValueError:
            return "Error: Invalid number"
    
    def calculate_sqrt(self, num):
        """计算平方根"""
        try:
            num = float(num)
            if num < 0:
                return "Error: Negative number"
            return sqrt(num)
        except ValueError:
            return "Error: Invalid number"
    
    def calculate_floor_division(self, a, b):
        """计算整除"""
        try:
            a = float(a)
            b = float(b)
            if b == 0:
                return "Error: Division by zero"
            return a // b
        except ValueError:
            return "Error: Invalid number"
    
    def calculate_modulo(self, a, b):
        """计算求余"""
        try:
            a = float(a)
            b = float(b)
            if b == 0:
                return "Error: Division by zero"
            return a % b
        except ValueError:
            return "Error: Invalid number"
    
    def on_button_click(self, char):
        """处理按钮点击事件"""
        current_text = self.result_var.get()
        
        if char == 'C':  # 清除
            self.result_var.set('')
        
        elif char == '=':  # 计算结果
            # 使用自定义计算函数替代eval
            tokens = current_text.split()
            if len(tokens) != 3:
                self.result_var.set("Error: Invalid expression")
                return
            
            a, operator, b = tokens
            result = self.calculate(a, b, operator)
            self.result_var.set(result)
        
        elif char == '√':  # 平方根
            if current_text:
                result = self.calculate_sqrt(current_text)
                self.result_var.set(result)
        
        elif char == '^2':  # 平方
            if current_text:
                result = self.calculate_square(current_text)
                self.result_var.set(result)
        
        elif char == '求整':  # 整除
            if ',' in current_text:
                a, b = current_text.split(',', 1)
                result = self.calculate_floor_division(a.strip(), b.strip())
                self.result_var.set(result)
            else:
                self.result_var.set("Error: Use format A,B")
        
        elif char == '求余':  # 求余
            if ',' in current_text:
                a, b = current_text.split(',', 1)
                result = self.calculate_modulo(a.strip(), b.strip())
                self.result_var.set(result)
            else:
                self.result_var.set("Error: Use format A,B")
        
        else:  # 数字和运算符
            # 添加空格分隔运算符，便于后续解析
            if char in '+-*/':
                new_text = current_text + ' ' + char + ' '
            else:
                new_text = current_text + char
            self.result_var.set(new_text)

if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()