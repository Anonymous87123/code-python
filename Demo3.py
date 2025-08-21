time = input("填数字,如1，2，3,现在给出数字：")
time1 = int(time)
name = "宇强传媒"
stock_price = 19.99
stock_code = "000001" 
factor = 1.1
result1 = factor ** time1
result2 = stock_price*result1
print(f"{name}当前的股价为{stock_price}元")
print(f"{time}天后，{name},即股票代号{stock_code}的股价将会涨到{result2:.6}元")