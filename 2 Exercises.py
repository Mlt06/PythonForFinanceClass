#Stock Information
ticker = "AAPL"
opening_price = 142.7
closing_price = 143.2
volume = 1200000
print(ticker, opening_price, closing_price, volume)

#Currency exchg
currency_pair = "EUR/USD"
buying_rate = 1.1825
selling_rate = 1.1830
print(currency_pair, buying_rate, selling_rate)

#Portfolio list
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

#Stock Dictionary
stock_details = {"ticker": "AAPL",
"opening_price": 142.7,
"closing_price": 143.2,
"volume": 1200000 }
print(stock_details)

#Bond dictionary
stock_details = {"issuer": "USTD",
"maturity_date": "31/10/2030"
"coupon rate" : 0.04
"face value" : 1000}
print(stock_details)


#LOOP
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
#this one works


#WHILE LOOP : Investment Growth
principal = 500
rate = 0.07
years = 0
while principal < 1000:
    principal *= (1 + rate)
    years += 1
print("Years needed:", years)

principal = 500
rate = 0.07
years = 11
future_value = principal * (1 + rate)**years
print("Value after 11 years", future_value)


#"IF" : Bond investment
bond_yield = 3.8
if bond_yield > 4.0:
    print("Buy the bond")
else:
    print("Do not buy the bond")

bond_yield = 3.8
if bond_yield >= 4.0:
    print("Buy the bond")
else:
    print("Do not buy the bond")
    
#ELIF and ELSE : Trading strat
pe_ratio = 17
if pe_ratio < 15:
    print("Buy the stock.")
elif pe_ratio > 25:
    print("Sell the stock.")
else:
    print("Hold the stock.")
    
pe_ratio = 17
if 14 <= pe_ratio <= 15:
    print("Buy the stock.")
elif 23 <= pe_ratio <= 27:
    print("Sell the stock.")
else:
    print("Hold the stock.")