stocks = ["AAPL", "MSFT", "GOOGL"]
stocks.append("IBM")
print(stocks)


stocks = ["TSLA", "AMZN", "FB"]
stocks.append("NVDA") #add only one element to a list
stocks.append("AMD")
print(stocks)


stocks = ["TSLA", "AMZN", "FB"]
stocks.extend(["NVDA","AMD"]) #add multiple elements to a list
print(stocks)

stock_details = {"ticker": "AAPL",
"opening_price": 142.7,
"closing_price": 143.2,
"volume": 1200000 }
print(stock_details)


stock_prices = [105, 107, 104, 106, 103]
for i in range(1, len(stock_prices)):
    daily_return = (stock_prices[i] - stock_prices[i-1]) / stock_prices[i-1]
    print(daily_return)

stock_prices = [105, 107, 104, 106, 103]
for i in range(1, len(stock_prices)):
    daily_return = (stock_prices[i] - stock_prices[i-1]) / stock_prices[i-1]
average_return = sum(daily_return)/len(daily_return)
print("Average return:", average_return)  #Doesnt work bcause we need to store the daily return data

stock_prices = [105, 107, 104, 106, 103]
for i in range(1, len(stock_prices)):
    daily_return = (stock_prices[i] - stock_prices[i-1]) / stock_prices[i-1]
    daily_return.append(daily_return)   #store the result as daily_return
average_return = sum(daily_return)/len(daily_return) if len(daily_return) > 0 else 0  #"if" prevent a division by zero 
print("Average return:", average_return)
#RESULT : "AttributeError: 'float' object has no attribute 'append'" bcause here daily_return is a float, so we have to create a variable

stock_prices = [105, 107, 104, 106, 103]
daily_returns = []
for i in range(1, len(stock_prices)):
    daily_return = (stock_prices[i] - stock_prices[i-1]) / stock_prices[i-1]
    daily_returns.append(daily_return)
average_return = sum(daily_returns) / len(daily_returns) if len(daily_returns) > 0 else 0
print("Average return:", average_return)


principal = 500
rate = 0.07
years = 11
future_value = principal * (1 + rate)**years
print("Value after 11 years", future_value)
