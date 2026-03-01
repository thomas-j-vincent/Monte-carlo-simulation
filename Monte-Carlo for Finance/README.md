# Monte-Carlo 

Although more efficient than solving high dimensional variables such as [PDE's](#pde) at the base of it, compared to using an analytical formula such as the [black sholes model](#black-scholes-model) it is less efficient as we have to simulate many variables from data processes and then take the average - making it in of itself a [stochastic variable](#stocastic-variable). Therefore the accuracy can be improved using variance reduction; this consists of two techniques [Antithetic variates](#antithetic-variates) and [control variates](#control-variates). Another way we can improve the Monte-carlo method is by using [Quasi-random](#quasi-random-numbers) numbers instead of [pseudo-random](#pseudo-random-numbers) numbers.

# Contents:  

- [Portfolio price simulation](#portfolio-price-simulation) 
- [Martingale strategy](#simulation-for-options-pricing)


# Portfolio price simulation

We can solve portfolio statistics using brownian motion such as:
- expected returns
- Risk metrics ([VaR](#var) [CVaR](#cvar))
- Downside risks
- and other probabilities of interest

We use the first code to look at a portfolio of assets, and their outcomes over a given time period - tool not modelling technique

## Code

First we import the required modules:
- math;
- numpy;
- pandas;
- datetime;
- scipy;
- matplotlib;
- yfinance

# Simulation for options pricing

This code computes the theoretical fair price of the option, if the price given is above the market price then the option may be underpriced - and a "good" deal, if the given price is below the market price the option may be overpriced - and a "bad" deal.

$$C_{0,i} = \text{exp}(- \int_0^T r_s ds)C_{T,i} = \text{exp}(-rT)C_{T,i}$$
for a particular simulation:
- $`\text{exp}(- \int_0^T r_s ds)`$ is the expectation of its discounted process, where the variable for the interest rate could change
- $`C_{T,i}`$ is the payoff at time T
equals the exponential of the discounted rate over the time multiplied by the payoff of the individual simulation

if we were to repeat the simulation $`\text{M}`$ times we can average the outcomes to:
$$C_{0}^{^} = \frac{1}{\text{M}} \sum_{i=1}^{\text{M}} C_{0,i}$$
$`\frac{1}{\text{M}}`$ sum all of the derivative prices

### Standard error: $SE(C_{0}^{^})$

$`C_{0}^{^}`$ is an estimate of the true value of option $`C_0`$ with error -as we are taking the average of randomly generated samples (this means the calculation itself is random). A measure of thsi error is the deviation of $`C_{0}^{^}`$ (standard error). This standard error can be estimated as the standard deviation of the call price ($`C_{0,i}`$) divided by the number of simulated paths ($`\text{M}`$)

$$`SE(C_{0}^{^}) = \frac{\sigma(C_{0,i})}{\sqrt{\text{M}}}`$$
$$`\sigma(C_{0,i}) = \sqrt{\frac{1}{\text{M}-1}\sum{i=1}^{\text{M}}(C_{0,i} - C_{0}^{^})^2}`$$

### European Call Option in the Black-Scholes World

Here we have a constant interest rate so the discount factor is $`exp(-rT)`$ and the stock dynamics are modelled with [Geometric Brownian Motion](#geometric-brownian-motion).

$$`dS_t =rS_tdt + \sigma(S_tdW_t)`$$

If we simulate this Geometric Brownian Motion process by simulating variables of the natural logarithm process of the stock price $`x_t = ln(S_t)`$, which is normally distributed. For the dynamics of the natural logarithm process of stock prices under Geometric Brownian Motion models you need to use [Ito's calculus](https://www.youtube.com/watch?v=Z5yRMMVUC5w)

$$`dx_t = vdt + \sigma dz_t, v = r- \frac{1}{2} \sigma^2`$$
We can then discretize (to make discrete) the Stochastic Differential Equation (change from infinitesimals $`dx, dt, dz`$ into small steps $` \Delta x, \Delta t, \Delta z `$)

$$` \Delta x = v\Delta t + \sigma \Delta z`$$
This means the exact solution and requires no approximation - as all the risk comes from the Brownian Motion process.

$` x_{t + \Delta t} = X_t + v(\Delta t) + \sigma(z_{t+\Delta t} - Z_t)`$ This tells us that the new time step is equal to the prior x + new change in time + the change in the random variables

in terms of the stock price S we have: 
$` S_{t+ \Delta t} = S_t exp(v \Delta t + \sigma (Z_{t+\Delta t} - Z_t)) `$ This equation shows that the next stock price is equal to the previous stock price multiplied by the exponential of the other terms. where all variants are normally distributed.

where: $`(z_{t+ \Delta t} ~ N(0, \Delta t) ~ \sqrt{\Delta t}N(0,1) ~ \sqrt{\Delta t} \epsilon_i)`$ (these are normally distributed )

## Code

First we import the required modules:
- math;
- numpy;
- pandas;
- datetime;
- scipy;
- matplotlib;
- yfinance

The parameters below should be able to be found from the options website, although implied volatility may need to be calculated.
The first parameter of datetime is the expiry date of the option. 
We add one to the date time as you can still trade on the day of expiry

``` python
S = 101.15   # stock price
K = 98.01    # strike price
vol = 0.0991 # implied volatility (%)
r = 0.01     # risk free rate (%)
N = 10       # number of time steps
M = 1000     # number of simulations (if increased the percentage error decreases)

market_value = 3.86 # market price of option
T = ((datetime.date(2027,3,17)- datetime.date.today()).days + 1)/365 #time in years
print(T)
```

``` python
#precompute constants
dt = T/N                    # Timestep is the time divided by the steps
nudt = (r - 0.5*vol**2)*dt  # nudt is (drift term r - 1/2 of the volatility^2) times by the timestep
volsdt = vol*np.sqrt(dt)    # volatility times the square root of time
lnS = np.log(S)             # logarithm of the stock price

#standard error placeholders
sum_CT = 0
sum_CT2 = 0

#monte carlo method
for i in range(M):      # for each simulation
    lnSt = lnS          # log st is the log of the stock price
    for j in range(N):  # for each timestep
        lnSt = lnSt + nudt + volsdt*np.random.normal() # calculate the next logst (add drift term and (volatility times the square root of time) multiplied by a random variable)

    ST = np.exp(lnSt)   # the exponential of the final payoff to get back to the stock price
    CT = max(0, ST - K) # the max between the stock price and the strike price
    sum_CT = sum_CT + CT  # take a sum of the previous ct and the next ct
    sum_CT2 = sum_CT2 + CT*CT # square the cts and add to the previous

#compute expectation and SE
C0 = np.exp(-r*T)*sum_CT/M # discount times sum of ct divided by the simulations
sigma = np.sqrt((sum_CT2 - sum_CT*sum_CT/M)*np.exp(-2*r*T)/(M-1))
SE = sigma/np.sqrt(M) # the standard error

print("call value is %{0} with SE +/- {1}".format(np.round(SE, 2)))
```

The fast solution is the same as the other "slow" method but is vectorised, making it faster but also less readable.

We then plot the graph:
`x1 = np.linspace(C0-3*SE, C0-1*SE, 100)` creates 100 evenly spaced values, from three standard errors below the mean to 1 standard error below the mean. (the left section of the normal distribution)
`x2 = np.linspace(C0-1*SE, C0+1*SE, 100)` creates the middle section - from one standard error below the mean to one standard error above the mean. The right side is defined with:`x3 = np.linspace(C0+1*SE, C0+3*SE, 100)`
Normal distribution values are calculated with: `s1 = stats.norm.pdf(x1, C0, SE)` now s1 contains the height of the normal cureve for each x-value in x1. This is then repeated with `s2` and `s3`.
To shade the areas under the curve we use: `plt.fill_between(x1, s1, color="tab:blue", label="> StDev")`, with this the leftmost area is blue - with a label of > stDev. The middle section is coloured cornflower blue and labelled 1 StDev, highlighting the +/- 1 region. The rightmost section is coloured blue and has no label as the first one is labelled for it.
We draw two vertical lines with: `plt.plot([C0,C0],[0, max(s2)*1.1], "k", label="theoretical value")` and `plt.plot([market_value,market_value],[0, max(s2)*1.1], "r", label="market value")` in black and red respectivley, comparing the theoretical price and the market price.
The y axis is then labelled "probability", the x axis "option price" The legend is rendered with `plt.legend()` and then shown with `plt.show()`
# Definitions:

## Black-Scholes model

## Stocastic Variable

## Antithetic Variates

## Control Variates

## Quasi-random numbers

## Pseudo-random numbers

## PDE

## VaR 

## CVaR

## Geometric Brownian Motion





