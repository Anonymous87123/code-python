import tkinter as tk
root = tk.Tk()
from math import sqrt, pow

class Calculator:
    def __init__(self, master):
        self.master = master
        self.result_var = tk.StringVar()
        self.master.title("Super Calculator")
        self.display = tk.Entry(master, textvariable=self.result_var, font=("Arial", 24), bd = 10,insertwidth=4,width = 14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)
        self.create_buttons()
    def create_button(self):
        buttons = [
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
            ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
            ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
            ('0',4,0),('.',4,1),('+',4,2),('=',4,3),
            ('√',5,0),('^2',5,1),('C',5,2),('求整',5,3),
            ('求余',6,0)
        ]
        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, padx=20, pady=20,width=5, height = 2,command=lambda t=text:self.on_button_click(t))
            button.grid(row=row, column=col,sticky='nsew')
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1)
def on_button_click(self,char):
    if char == 'C':
        self.result_var.set('')
    elif char == '=':
        try:
            expression = self.result_var.get()
            result = eval(expression)
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set('Error')
    elif char == '√':
        try:
            value = float(self.result_var.get())
            result = sqrt(value)
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set('Error')
    elif char == '^2':
        try:
            value = float(self.result_var.get())
            self.result_var.set(pow(value, 2))
        except Exception as e:
            self.result_var.set('Error')
    elif char == '求整':
        try:
            values = self.result_var.get().split(',')
            if len(values) == 2:
                num1 = float(values[0])
                num2 = float(values[1])
                self.result_var.set(num1 // num2)
            else:
                self.result_var.set('输入格式:A,B')
        except ValueError:
            self.result_var.set('Error')
    elif char == '求余':
        try:
            values = self.result_var.get().split(',')
            if len(values) == 2:
                num1 = int(values[0])
                num2 = int(values[1])
                self.result_var.set(num1 % num2)
            else:
                self.result_var.set('输入格式:A,B')
        except ValueError:
            self.result_var.set('Error')
    else:
        current_text = self.result_var.get()
        new_text = current_text + str(char)
        self.result_var.set(new_text)
if __name__ == '__main__':
    root = ()
    calc = Calculator(root)
    root.mainloop()
        
