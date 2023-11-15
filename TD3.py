#Object-Oriented programming (OOP)

#class : brueprint for creating objects
#object : specific instance of a class
#attribute: properties or specifics of the financial instrument
#method: actions or calculations one can perform on the financial instrument

#Stock and Dividend

class stock:
    def __init__(self, name, price, dividend):
        self.name = name
        self.price = price
        self.dividend = dividend
    def yield_dividend(self):
        return self.dividend / self.price

apple_stock = Stock('AAPL', 150, 0.82)
print(apple_stock.yield_dividend())





#ex 2: Financial instrument portfolio
class portfolio:
    def __init__(self, assets) : 
        self.assets = [assets] 
        
    def add_instrument(self, a_2, a_3, a_4) :
        self.assets.extend([a_2, a_3, a_4]) #ajouter plusieurs assets à la liste
        
pf1 = portfolio('AAPL')
a_2 = 'MSFT'
a_3 = 'AMZN'
a_4 = 'GOOGL'

pf1.add_instrument(a_2, a_3, a_4)
print(pf1.assets)

#maintenant il faut aujouter la fonction de total_value
class portfolio:
    def __init__(self, assets) : 
        self.assets = [assets] 
        
class a_2 : 
    def __init__(self, qty, price):
        self.qty = qty
        self.price = price 

class a_3 : 
    def __init__(self, qty, price):
        self.qty = qty
        self.price = price 
        
class a_3 : 
    def __init__(self, qty, price):
        self.qty = qty
        self.price = price 

    def add_instrument_2(self, a_2, a_3, a_4) :
        self.assets.extend([a_2, a_3, a_4])

def value_assets(self) : 
    return 
#Trop de données et de classes

#utilisons class stock
class Stock_p: #we use another name bcause of the stock class above
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Portfolio_1: 
    def __init__(self) : 
        self.assets = []  #une liste pour stocker des instruments financiers
        
    def add_instruments(self, instruments):
        self.assets.extend(instruments) 
    
    def total_value(self, current_prices): #during the execution we will have to define current_prices as a dictionnary using {} ; e.g. : 'dico={'a1' : price1, 'a2', price2} 
        total = 0 #on commence à 0 la valeur actuelle
        for asset in self.assets: #this iterate through the list self.asset. At each iteration, there is an "asset" that contain a fin instrmt (in the class 'Stock_p')
            if asset.name in current_prices:  #check if the current price of this asset is available in the price dictionary "current_price"
                total += current_prices[asset.name] #this add the asset's price to the total value. It uses 'asset_name' as a key to access to the current price in the dictionnary
            else : 
                print("price not available for {asset.name}") #to prevent any bug
        return total

a1 = Stock_p("US30", 34900)
a2 = Stock_p("WTI", 77)
a3 = Stock_p("NASDAQ", 15800)

current_prices = {'US30': 34900,'WTI' : 77 , 'NASDAQ' : 15800}
pf1 = Portfolio_1()

pf1.add_instruments(a1, a2, a3)
print(pf1.total_value(current_prices))

#THIS CODE DOESN'T WORK : bcause add_instrument takes only 2 positionnal aegs (hmslef and 'instruments') => to make it works we have to write '*istruments' so the methods takes in account a variable nmer of arguments



#Second version of the code : 
class Stock_p: 
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Portfolio_1: 
    def __init__(self) : 
        self.assets = []  #defin the list self.assets
        
    def add_instruments(self, *instruments): #now the methods can take multiple argument to extend the asset list
        self.assets.extend(instruments) 
    
    def total_value(self, current_prices): 
        total = 0
        for asset in self.assets: #pour chaque asset dans cette liste self.assets
            if asset.name in current_prices: #si il y a un prix correspondant au nom de l'asset 
                total += current_prices[asset.name] #alors on l'ajoute au total
            else : 
                print("price not available for {asset.name}") 
        return total

a1 = Stock_p("US30", 34900)
a2 = Stock_p("WTI", 77)
a3 = Stock_p("NASDAQ", 15800)

current_prices = {'US30': 34900,'WTI' : 77 , 'NASDAQ' : 15800}
pf1 = Portfolio_1()

pf1.add_instruments(a1, a2, a3)
print(pf1.total_value(current_prices))

#it works but can be shorter. Maybe we could merge the dictionary to the Sock_p allowing to only define the dictionary and not a1, a2, a3 



#EXO 3 : CURRENCY CONVERSION

class Currency :
    def __init__(self, currency_pair) :
        self.currency_pair = currency_pair

class CurrencyConverter :
    def __init__(self) : 
        self.conversion_rates = {} #as {'EUR_USD': 1.08}
    def add_conversion_rates(self, currency_pair, *c_rates) : 
        self.conversion_rates[currency_pair] = c_rates #self.dictionary[]=value is the action to add smtg in a dict
         #but this allows to add only one pair we need the '.update' methods that allows us to add multiple key-value pairs from a dictionnary to another one
    
    def convert(self, CurrencyConverter): #we have to execute amount*rate
        converted_amount = 0
        for conversion_rates in self.conversion_rates : 
            if 
        return c_rates*amount
    

#2ND version

class CurrencyConverter :
    def __init__(self) : 
        self.pair_and_conversion_rates = {} #as {'EUR_USD': 1.08}
    
    def add_pair_and_conversion_rates(self, rates_dict) : 
        self.pair_and_conversion_rates.update(rates_dict) #we can now add multiple key-values
    
    
    def convert(self, c_rates, amount): 
        converted_amount = 0 #initialisation (du montant converti) à 0
        for pair_and_conversion_rates in self.pair_and_conversion_rates : #pour chaque couple dans le dico 
            return 
        return c_rates*amount
    

#A RETRAVAILLER mais voici une suggestion de chatGPT pour le compléter : 
class CurrencyConverter:
    def __init__(self):
        self.pair_and_conversion_rates = {}  

    def add_pair_and_conversion_rates(self, rates_dict):
        self.pair_and_conversion_rates.update(rates_dict)  

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount  
        
        conversion_rate = self.pair_and_conversion_rates.get(f"{from_currency}_{to_currency}")
        if conversion_rate is None:
            return None 

        converted_amount = amount * conversion_rate
        return converted_amount  
#cette suggestion fonctionne




#MATHEMATICAL TOOLS with NUMPY

#EX1 Stock price simulations

import numpy as np
import numpy_financial as npf

#as n tends to infinity the sum of a random experience tends to a normal distribution (Cf prépa) so we can use the function of generation of random sample from a normal distribution `numpy.random.normal()' (Cf NotesPython.docx)

#random series of D_returns
n = 10000
m = 0.001
S = 0.02
daily_return = np.random.normal(m, S, n) 
print(daily_return[:100])  #prints the first 100 daily returns





#Stock price simu
n = 10000
m = 0.001
S = 0.02
daily_return = np.random.normal(m, S, n) 

#we can calculate stock price as follows : Soit n entier, pour i allant de 1 à n, Pn = Po ∙ ∏(1+r_i)
l = int(input("Price after how many days ? ")) #'int()' to set it as integers inputs
initial_price = float(input("enter initial price of your stock : ")) #'float()' to set it as floats
stock_price= initial_price
for i in range(2,l+1) :  #the range function in Python excludes the end value ( i€[2;l[ ), so with l+1 i€[2;l]
    stock_price = stock_price * (1+daily_return[i-1])  #Cf PythonNotes to know why i-1

print("estimated stock price after {} days : {:.2f}".format(l, stock_price))
