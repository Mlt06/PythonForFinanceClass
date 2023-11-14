# Importing necessary libraries
import numpy as np
import numpy_financial as npf
import pandas as pd

#Net Present Value
cash_flows = np.array([-100000, 20000, 25000, 30000, 35000, 40000])
discount_rate = 0.1
npv = npf.npv(discount_rate, cash_flows)
print("Net Present Value:", npv)

#Calculatinf internal rate of return (IRR)
irr = npf.irr(cash_flows)
print("Internal Rate of return:", irr)

#Using pandas Datafram for financial analysis
data = {"Revenue": [200000, 250000, 300000, 350000, 400000],
        "Cost" : [150000, 175000, 200000, 225000, 250000]}
df = pd.DataFrame(data)
df["Profit"] = df["Revenue"] - df["Cost"]
print(df)


#SIMPLE AND COMPOUND INTRST
# Simple Interest
principal = 10000 # initial amount of money
rate = 0.05 # interest rate
time = 5 # time in years
simple_interest = principal * rate * time
print("simple interest :", simple_interest)

# Compound Interest
compound_interest = principal * ((1 + rate) ** time - 1)
print("Compound Interest :", compound_interest)




# Calculating Moving Averages (used to smooth out ST fluctuations and highlight LT trends)

# Sample price data 
prices = pd.Series([1, 3, 7, 9, 12, 14, 16, 19, 23, 26])

# Calculating 3-day simple moving average
moving_average = prices.rolling(window=3).mean()
print("Moving Average:/n", moving_average)




#Calculating Portfolio Variance (w^T*Σ*w où w^T la transposée du vecteur de pondération Σ la matrice de covariance des rendements w le vecteur de pondération)
# Define wheights, returns and covariance matrix of the portfolio assets
weights = np.array([0.4, 0.6]) #this is for two assets
returns = np.array([0.1, 0.12]) #expected returns
cov_matrix = np.array([[0.1, 0.03], [0.03, 0.12]])

#Calculate the portfolio variance
portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
print("Portfolio Variance:", portfolio_variance)





