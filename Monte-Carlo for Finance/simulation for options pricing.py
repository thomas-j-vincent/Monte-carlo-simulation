import math
import numpy as np
import pandas as pd
import datetime 
import scipy.stats as stats
import matplotlib.pyplot as plt
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
endDate = datetime.datetime.now()
startDate = endDate - datetime.timedelta(days = 300)

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

#plt.plot(portfolio_sims)
#plt.ylabel("portfolio value ($)")
#plt.xlabel("Days")
#plt.title("Monte-Carlo simulation of a stock portfolio")

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
#plt.show()

#plt.plot(ST)
plt.ylabel("Stock Price")
plt.xlabel("Time steps over 1 year")
plt.title("MC simulation of a Stock Price")
plt.show()

S = 101.15 #stock price
K = 98.01 #strike price
vol = 0.0991 # volatility
r = 0.01 #risk free rate
N = 10 # number of time steps
M = 1000 # number of simulations (if increased error decreases)

market_value = 3.86 # market price of option
T = ((datetime.date(2022,3,17)- datetime.date.today()).days + 1)/365 #time in years
print(T)

#precompute constants
dt = T/N
nudt = (r - 0.5*vol**2)*dt
volsdt = vol*np.sqrt(dt)
lnS = np.log(S)

#standard error placeholders
sum_CT = 0
sum_CT2 = 0

#monte carlo method
for i in range(M):
    lnSt = lnS
    for j in range(N):
        lnSt = lnS + nudt + volsdt*np.random.normal()

    ST = np.exp(lnSt)
    CT = max(0, ST - K)
    sum_CT = sum_CT + CT
    sum_CT2 = sum_CT2 + CT*CT

#compute expectation and SE
C0 = np.exp(-r*T)*sum_CT/M
sigma = np.sqrt( (sum_CT2 - sum_CT*sum_CT/M)*np.exp(-2*r*T) / (M-1) )
SE = sigma/np.sqrt(M)

print("call value is %{0} with SE +/- {1}".format(np.round(SE, 2)))

#fast method

N = 1
dt = T/N
nudt = (r - 0.5*vol**2)*dt
volsdt = vol*np.sqrt(dt)
lnS = np.log(S)

#monte carlo method
Z = np.random.normal(size=(N, M))
delta_lnSt = nudt + volsdt*Z
lnSt = lnS + np.cumsum(delta_lnSt, axis=0)
lnSt = np.concatenate( (np.full(shape=(1, M), fill_value=lnS), lnSt) )

#compute expectation and SE
ST = np.exp(lnSt)
CT = np.maximum(0, ST - K)
C0 = np.exp(-r*T)*np.sum(CT[-1])/M

sigma = np.sqrt( np.sum( (CT[-1] - C0)**2) / (M-1) )
SE = sigma/np.sqrt(M)

print("Call value is ${0} with SE +/- {1}".format(np.round(SE, 2)))

x1 = np.linspace(C0-3*SE, C0-1*SE, 100)
x2 = np.linspace(C0-1*SE, C0+1*SE, 100)
x3 = np.linspace(C0+1*SE, C0+1*SE, 100)

s1 = stats.norm.pdf(x1, C0, SE)
s2 = stats.norm.pdf(x2, C0, SE)
s3 = stats.norm.pdf(x3, C0, SE)

plt.fill_between(x1, s1, color="tab:blue", label="> StDev")
plt.fill_between(x2, s2, color="cornflowerblue", label="1 StDev")
plt.fill_between(x3, s3, color="tab:blue")
plt.plot([C0,C0],[0, max(s2)*1.1], "k", label="theoretical value")
plt.plot([market_value,market_value],[0, max(s2)*1.1], "r", label="market value")
plt.ylabel("probability")
plt.xlabel("option price")
plt.legend()
plt.show()
#plt.plot(ST)