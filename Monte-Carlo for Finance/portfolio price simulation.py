import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yf 

def get_data(stocks, start, end):
    #stockData = pdr.get_data_yahoo(stocks, start, end)
    stockData = yf.download(stocks, start=start, end=end)
    stockData = stockData['Close']
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

stockList = ['CBA', 'BHP', 'TLS', 'NAB', 'WBC', 'STO']
stocks = [stock + '.AX' for stock in stockList] # .ax for australian stocks
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 300)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)

weights = np.random.random(len(meanReturns))
weights /= np.sum(weights)

mc_sims = 100 #number of simulations
T = 100 # timeframe in days

meanM = np.full(shape=(T, len(weights)), fill_value=meanReturns)
meanM = meanM.T

portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0)
initialPortfolio = 10000

for m in range(0, mc_sims):
    #monte carlo loops
    Z = np.random.normal(size=(T, len(weights)))
    L = np.linalg.cholesky(covMatrix)
    dailyReturns = meanM + np.inner(L, Z)
    portfolio_sims[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)* initialPortfolio

plt.plot(portfolio_sims)
plt.ylabel("portfolio value ($)")
plt.xlabel("Days")
plt.title("Monte-Carlo simulation of a stock portfolio")

def mcVaR(returns, alpha = 5): # inputs pandas series
    if isinstance(returns, pd.Series):
        return np.percentile(returns, alpha)
    else:
        raise TypeError("expected pandas data series.")
# outputs percentile of returns distribution to a given confidence level

def mcCVaR(returns, alpha = 5): # inputs pandas series
    if isinstance(returns, pd.Series):
        belowVaR = returns <= mcVaR(returns, alpha = alpha)
        return returns[belowVaR].mean()
    else:
        raise TypeError("expected pandas data series.")
# outputs CVaR or Expected shortfall to a given confidence level

portResults = pd.Series(portfolio_sims[-1,:])
VaR = initialPortfolio - mcVaR(portResults, alpha = 5)
CVaR = initialPortfolio - mcCVaR(portResults, alpha = 5)

print("VaR ${}".format(round(VaR,2)))
print("CVaR ${}".format(round(CVaR,2)))
plt.show()