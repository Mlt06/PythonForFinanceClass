#1. Financial Time series 

#1st Version
dates = ["4th January", "5th January", "6th January"]
stock_prices = [155, 156, 153]

def calculate_average(prices) :
    return sum(prices) / len(prices)

average_price = calculate_average(stock_prices)
print(f"average stock price : ${average_price}")

def calculate_max(prices) :
    return max(prices)

highest_price = calculate_max(stock_prices)
print(f"highest stock price : ${highest_price}")

dates.extend(["7th January","8th January"])
stock_prices.extend([157, 152])

for date, price in zip(dates, stock_prices):
        print(f"{date} : ${price}") #ceci a permis d'extraire chq élément individuel (date et price)

def trend(dates, stock_prices): 
     previous_price = stock_prices[0] #on définit le prix précedent avec le premier de la série de prix
     for price in stock_prices[1:] : 
          if price > previous_price : 
               print("price increase")
          elif price < previous_price:
               print("price decrease")
          else: 
               print("price is stable")
               previous_price = price 

        #ce code ne nous donne pas la tendance => pour avoir la tendance on peut compter le nombre de jour haussiers, baissier et stagnants

#2nd Version

dates = ["4th January", "5th January", "6th January"]
stock_prices = [155, 156, 153]

def calculate_average(prices) :
    return sum(prices) / len(prices)

average_price = calculate_average(stock_prices)
print(f"average stock price : ${average_price}")

def calculate_max(prices) :
    return max(prices)

highest_price = calculate_max(stock_prices)
print(f"highest stock price : ${highest_price}")

dates.extend(["7th January","8th January"])
stock_prices.extend([157, 152])

for date, price in zip(dates, stock_prices):
        print(f"{date} : ${price}")

def trend_2(dates, stock_prices): 
    previous_price = stock_prices[0]
    up_d = 0
    down_d = 0
    stable_d = 0 #on initialise chq variable
    for price in stock_prices[1:]:
        if price > previous_price :
            up_d += 1
        elif price < previous_price :
            down_d += 1 
        else: 
            stable_d += 1
        previous_price = price
    
    if up_d > down_d and up_d > stable_d : 
         print("Bullish")
    elif down_d > up_d and down_d > stable_d :
         print("Bearish")
    elif stable_d > up_d and stable_d > down_d :
         print("Sideways")
    else : 
         print("No clear tendancy")

trend = trend_2(dates, stock_prices)               



#Financial Time Series 

dates = ["4th January", "5th January", "6th January"]
stock_prices = [155, 156, 153]

for date, price in zip(dates, stock_prices):
        print(f"{date} : ${price}")

def calculate_average(prices):
     return sum(prices) / len(prices)

average_price = calculate_average(stock_prices)
print(f"Average Stock Price: ${average_price}")
