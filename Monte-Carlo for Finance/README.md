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
provides an easy way to simulate as many possible outcomes, this is useful in finance as a tool to price derivatives because analytical analysis is not always possible due to multiple random factors and having to incorperate more realistic asset price processes such as jumps in price. 

We can use monte carlo to price derivatives, where brownian motion is representative of risk neutral probabilities

valuation by simulation - risk neutral pricing methodolody states that the value of an option = risk-neutral expectation of its discounted payoff. This can be estimated by computitng the average of a large number of dicounted payoffs.

$`C_{0,i} = \text{exp}(- \int_0^T r_s ds)C_{T,i} = \text{exp}(-rT)C_{T,i}`$
for a simulation = expectation of its discounted process 


## Code

First we import the required modules:
- math;
- numpy;
- pandas;
- datetime;
- scipy;
- matplotlib;
- yfinance

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





