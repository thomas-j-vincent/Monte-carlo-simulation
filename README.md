# Monte-carlo-simulation

The Monte-carlo simulation is a method of predicting outcomes using random numbers by running numerous simulations and taking a mean of the results, the main concept being using randomness to solve deterministic problems(problems where no randomness is involved). It is used to "brute-force" solutions to problems too complex to solve via mathematical analysis, under the topics; optimisation, numerical integration and probability distribution such as the number of Pi. Another usecase is to determine the risk of a strategy, such as trading or gambling as the monte carlo simulation can run through many possible outcomes and calculate the probability of one being the outcome that you want.
## Contents:  

- [Simple bettor](#simple-bettorpy) 
- [Martingale strategy](#martingale-strategypy)
- [Multiplier optimiser](#multiplier-optimiserpy)
- [Main.py](#main.py) 
- [d'Alembert strategy](#dalembert-strategypy)
- [Monter-carlo grapher](#monte-carlo-grapherpy)
- [LaBouchere system](#labouchere-systempy)

## Simple bettor.py

Simple bettor is a bettor that bets the same amount whether they win or lose, this results in a strategy that is very stable and results in a low bust ratio - but also a low-ish amount of profit that is obtainable. The image below shows the path of 1000 bettors over 100 wagers, as you can see at the top end there is profit to be had, (~3000 units) and also a loss of ~3000. This may make it seem like a perfect bettor however if we were to change the `wagerCount` from 100 to 100000 (see second image). You can see that the profit almost maxes out at around 3000 up or down (For the majority)
![Image shows the path of 1000 bettors over 100 wagers](/images/SimpleBettorFigure1.png)
![Image shows the path of 1000 bettors over 100000 wagers](/images/SimpleBettorFigure2.png)

### Code

We import three modules: 
- Random, which is used to act as a dice to pick a number from 1- 100
- Matplotlib; which is used for plotting the graph
- Pyplot; which is the specific graph that we use

The function rollDice is the dice function, and has three outcomes: if roll is 100, the player loses and the function returns false, if the roll is less than 50, the player loses and the function returns false, and if the number is less than 100 but larger than 50 the player wins and the function returns true. Giving a 49% chance of winning.

The function simple_bettor takes three parameters: `funds, initial_wager, wager_count`
- funds is the starting amount that each bettor starts out with
- initial_wager is the amount the bettors are permitted to bet each round
- wager_count is the amount of bets they are allowed to place

We start off creating a few variables, `global simple_busts` and `global simple_profits` which are used to track how many times the bettors go broke or make a profit (these values are returned at the end of the program). 
`value` is set as the `funds`, so we can take away or add on winning or losing bets to return a final value
`wager` is set as `initial_wager`, the wager we will place each time.
`wX` and `vY` are lists of coordinates, passed onto the plotter so that the result can be graphed. 
`currentWager` is set at 1, but could just as easily be 0.

We then enter the main portion of the function: 
`while currentWager <= wager_count:` means that for the amount of wagers each bettor has to place
    `if rollDice():` is true:
        `value += wager`we add the wager value to the overall value (as profit)
        `wX.append(currentWager)`we then append the currentWager to wX and value to vY
        `vY.append(value)`
    `else:` if roll dice is false (the bettor has lost the bet)
        `value -= wager`we subtract the wager value from the overall value (as loss)
        `wX.append(currentWager)`we then append the currentWager to wX and value to vY
        `vY.append(value)`
`if value <= 0:` if the bettor has lost all their money and has gone broke
    `value = 0` set the overall value to 0
    `simple_busts += 1` add one to the "gone broke" counter
`plt.plot(wX, vY)` plot the graph
`if value > funds:` if the value is greater than original funds
    `value = 0` reset the value
    `simple_profits += 1` add one to the profit counter

we then define more variables that are used to set the experiment:
- x is 0, used for the counter - rerunning the experiment each time
- sampleSize, sets the amount of times the experiment reruns 
- startingFunds, wagerSize, wagerCount are all parameters that countrol the simple bettor

In the next loop we tell the experiment what to do when we run the program
`while True:` - since the program starts until it is stopped (with ctrl + c)
    `simple_busts` and `simple_profits` are set to 0.0, allowing a decimal
    The next loop is while the program hasn't run the full length
        `simple_bettor(startingFunds, wagerSize, wagerCount)` calls the function with the above parameters
        `x+= 1` adds one to x so that the program doesn't run forever
    we then print the bust chance and the profit chance as a percentage
    we then show the graph with labels on its two axis.

## Martingale strategy.py

The Martingale strategy is a bettor that doubles the bet if they lose supposidly because if you lose the first flip you are more likely to win the second flip (this is not true, with 50-50 odds each flip is independent of the one before). This however results in a larger amount of busts that are possible, and also a higher amount of profit available. The image below shows the path of 1000 bettors over 100 wagers, as you can see there is more profit to be had than with the simple bettor (~7000 units), but with a potential loss of 10000. You may be inclined to only use this bettor and cast away with the simple bettor however, if we were to change `wagerCount` from 100 to 100000 (see second image) you can see that the profit almost maxes out at around 7000 up, but with an increased percentage of bettors going broke (4.5%)
![Image shows the path of 1000 bettors over 100 wagers](/images/DoublerBettorFigure1.png)
![Image shows the path of 1000 bettors over 100000 wagers](/images/DoublerBettorFigure2.png)

### Code

We import three modules: 
- Random, which is used to act as a dice to pick a number from 1- 100
- Matplotlib; which is used for plotting the graph
- Pyplot; which is the specific graph that we use

The function rollDice is the dice function, and has three outcomes: if roll is 100, the player loses and the function returns false, if the roll is less than 50, the player loses and the function returns false, and if the number is less than 100 but larger than 50 the player wins and the function returns true. Giving a 49% chance of winning.

The function doubler_bettor takes three parameters: `funds, initial_wager, wager_count`
- funds is the starting amount that each bettor starts out with
- initial_wager is the amount the bettors are permitted to bet each round
- wager_count is the amount of bets they are allowed to place

We start off creating a few variables, `global doubler_busts` and `global doubler_profits` which are used to track how many times the bettors go broke or make a profit (these values are returned at the end of the program). 
`value` is set as the `funds`, so we can take away or add on winning or losing bets to return a final value
`wager` is set as `initial_wager`, the wager we will place each time.
`wX` and `vY` are lists of coordinates, passed onto the plotter so that the result can be graphed. 
`currentWager` is set at 1, but could just as easily be 0.
`previousWager` is set as `"win"` This is needed as it depends on the previous outcome whether the bettor doubles the wager or not.
`previousWagerAmount` is set as `initial_wager`, also required because you are not just doubling the initial wager - it could have been doubled more than once.

We then enter the main portion of the function: 
`while currentWager <= wager_count:` means that for the amount of wagers each bettor has to place
    `if previousWager` is `"win"` if the bettor won the last bet
        `if rollDice():` is true:
            `value += wager`we add the wager value to the overall value (as profit)
            `wX.append(currentWager)`we then append the currentWager to wX and value to vY
            `vY.append(value)`
        `else:` if roll dice is false (the bettor has lost the bet)
            `value -= wager`we subtract the wager value from the overall value (as loss)
            `previousWager = "loss"` we set the previous wager to loss so that we know to double the bet next time.
            `previousWagerAmount = "wager"` we set the previous wager, so we know what to double
            `wX.append(currentWager)`we then append the currentWager to wX and value to vY
            `vY.append(value)`
            `if value <= 0:` if the bettor has lost all their money and has gone broke
            `wX.append(currentWager)`we then append the currentWager to wX and value to vY
            `vY.append(value)`
            `doubler_busts += 1` add one to doubler busts (returned later)
            `break` go back to the start 
    `elif previousWager == "loss"` if the bettor lost the last bet
        `if rollDice():` is true:
            `wager = previousWagerAmount * 2` multiply the last wager by two - and set it as the current wager
            `if (value - wager) < 0:` if the current wager is larger than the money the bettor has left
                `wager = value` set the wager to all the money we have left instead
            `value += wager` add the wager to the value, so we know what we have left
            `wager = "initial_wager"` as we have won, we reset to the original wager
            `previousWager = "win"` we set the previous wager so we know there is no need to double
            `wX.append(currentWager)`we then append the currentWager to wX and value to vY
            `vY.append(value)`
        `else:` if the bettor loses =:
            `wager = previousWagerAmount * 2` multiply the last wager by two - and set it as the current wager
            `if (value - wager) < 0:` if the current wager is larger than the money the bettor has left
                `wager = value` set the wager to all the money we have left instead
            `value -= wager` subtract the wager from the value, so we know what we have left
            `previousWagerAmount = wager` we set the previous wager so we know what to double - or not - next.
            `wX.append(currentWager)`we then append the currentWager to wX and value to vY
            `vY.append(value)`
            `if value <= 0:` if the bettor has lost all their money and has gone broke
                `wX.append(currentWager)`we then append the currentWager to wX and value to vY
                `vY.append(value)`
                `doubler_busts += 1` add one to doubler busts (returned later)
                `break` go back to the start
            `previousWager = "loss"` we set the previous wager to loss so that we know to double the bet next time.
            `previousWagerAmount = "wager"` we set the previous wager, so we know what to double
            `wX.append(currentWager)`we then append the currentWager to wX and value to vY
            `vY.append(value)`
    `currentWager += 1` add one to currentWager, the bettor has successfully placed a bet
`plt.plot(wX, vY)` plot the graph
`if value > funds:` if the value is greater than original funds
    `doubler_profits += 1` add one to the profit counter

we then define more variables that are used to set the experiment:
- x is 0, used for the counter - rerunning the experiment each time
- sampleSize, sets the amount of times the experiment reruns 
- startingFunds, wagerSize, wagerCount are all parameters that countrol the simple bettor

In the next loop we tell the experiment what to do when we run the program
`while True:` - since the program starts until it is stopped (with ctrl + c)
    `doubler_busts` and `doubler_profits` are set to 0.0, allowing a decimal
    The next loop is while the program hasn't run the full length
        `doubler_bettor(startingFunds, wagerSize, wagerCount)` calls the function with the above parameters
        `x+= 1` adds one to x so that the program doesn't run forever
    we then print the bust chance and the profit chance as a percentage
    we then show the graph with labels on its two axis.

## Multiplier optimiser.py

The Multiplier optimiser is a bettor that is based on the doubler bettor, but by using the monte-carlo strategy the we can optimise the multiplier to find the best ratio of bust-rate to profit-rate.

### Code

We import only one module this time: 
- Random, which is used to act as a dice to pick a number from 1- 100

The function rollDice is the dice function, and has three outcomes: if roll is 100, the player loses and the function returns false, if the roll is less than or equal to 50, the player loses and the function returns false, and if the number is less than 100 but larger than 50 the player wins and the function returns true. Giving a 49% chance of winning.

The function doubler_bettor takes three parameters: `funds, initial_wager, wager_count`
- funds is the starting amount that each bettor starts out with
- initial_wager is the amount the bettors are permitted to bet each round
- wager_count is the amount of bets they are allowed to place

We start off creating a few variables, `global multiple_busts` and `global multiple_profits` which are used to track how many times the bettors go broke or make a profit (these values are returned at the end of the program). 
`value` is set as the `funds`, so we can take away or add on winning or losing bets to return a final value
`wager` is set as `initial_wager`, the wager we will place each time.
`currentWager` is set at 1, but could just as easily be 0.
`previousWager` is set as `"win"` This is needed as it depends on the previous outcome whether the bettor doubles the wager or not.
`previousWagerAmount` is set as `initial_wager`, also required because you are not just multiplying the initial wager - it could have happened more than once.

We then enter the main portion of the function: 
`while currentWager <= wager_count:` means that for the amount of wagers each bettor has to place
    `if previousWager` is `"win"` if the bettor won the last bet
        `if rollDice():` is true:
            `value += wager`we add the wager value to the overall value (as profit)
        `else:` if roll dice is false (the bettor has lost the bet)
            `value -= wager`we subtract the wager value from the overall value (as loss)
            `previousWager = "loss"` we set the previous wager to loss so that we know to double the bet next time.
            `previousWagerAmount = "wager"` we set the previous wager, so we know what to double
            `if value <= 0:` if the bettor has lost all their money and has gone broke
            `multiplier_busts += 1` add one to multiplier busts (returned later)
            `break` go back to the start 
    `elif previousWager == "loss"` if the bettor lost the last bet
        `if rollDice():` is true:
            `wager = previousWagerAmount * random_multiple` multiply the last wager by a random multiple - and set it as the current wager
            `if (value - wager) < 0:` if the current wager is larger than the money the bettor has left
                `wager = value` set the wager to all the money we have left instead
            `value += wager` add the wager to the value, so we know what we have left
            `wager = "initial_wager"` as we have won, we reset to the original wager
            `previousWager = "win"` we set the previous wager so we know there is no need to double
        `else:` if the bettor loses =:
            `wager = previousWagerAmount * random_multiple` multiply the last wager by a random multiple - and set it as the current wager
            `if (value - wager) < 0:` if the current wager is larger than the money the bettor has left
                `wager = value` set the wager to all the money we have left instead
            `value -= wager` subtract the wager from the value, so we know what we have left
            `previousWagerAmount = wager` we set the previous wager so we know what to double - or not - next.
            `if value <= 0:` if the bettor has lost all their money and has gone broke
                `mutiplier_busts += 1` add one to mulitplier busts (returned later)
                `break` go back to the start
            `previousWager = "loss"` we set the previous wager to loss so that we know to double the bet next time.
    `currentWager += 1` add one to currentWager, the bettor has successfully placed a bet
`if value > funds:` if the value is greater than original funds
    `multiplier_profits += 1` add one to the profit counter

we then define more variables that are used to set the experiment:
- x is 0, used for the counter - rerunning the experiment each time
- sampleSize, sets the amount of times the experiment reruns 
- startingFunds, wagerSize, wagerCount are all parameters that countrol the simple bettor

In the next loop we tell the experiment what to do when we run the program
`while True:` - since the program starts until it is stopped (with ctrl + c)
    `multiplier_busts` and `multiplier_profits` are set to 0.0, allowing a decimal
    `multipleSampleSize` and `currentSample` are set to numbers which are passed to the function
    `random_multiple` is defined as a integer between 0.1 and 10.0
    The next loop is while the program hasn't run the full length
        `multiple_bettor(startingFunds, wagerSize, wagerCount)` calls the function with the above parameters
        `x+= 1` adds one to x so that the program doesn't run forever
    If the bust percentage and profit percentage are greater than the lower bust and higher profit:
        we then print the bust chance and the profit chance as a percentage
        we then write it to `monteCarlo-multiplierOptimiser.csv` so it can be graphed with the grapher
    If the multiplier doesn't pass these qualifiers:
        if the bust rate or profit rate is not 100, or 0:
            add it to the `monteCarlo-multiplierOptimiser.csv` so it can be graphed using the grapher.


## Main.py

Main.py is used to compare the three multiplier-based betting strategies, and returns its busts and profits per sample size. The image below shows the graphical output of the program - excluding the busts and profits which are printed to the terminal. In this image simple bettor is in black, double bettor is in blue, and multiple bettor is in magenta. As you can see the double bettor and the multiple bettor result in aproximately the same profits; but the multiple bettor often recovers more quickly - reducing its chances of going broke.
![Image shows the comparison of the three strategies](/images/MainFigure1.png)

### Code

We import four modules: 
- Random, which is used to act as a dice to pick a number from 1- 100
- Matplotlib; which is used for plotting the graph
- Pyplot; which is the specific graph that we use
- csv; which helps us to find the optimum multiplier from the multiplier optimiser csv

The function rollDice is the dice function, and has three outcomes: if roll is 100, the player loses and the function returns false, if the roll is less than 50, the player loses and the function returns false, and if the number is less than 100 but larger than 50 the player wins and the function returns true. Giving a 49% chance of winning.

The function findOptimum() is the funciton for reading the csv and picking the best multiplier by scoring each line based on its bust rate and profit rate. It works as follows:
`best_multiplier` is defined as none, as we havent found a multiplier yet
`best_score` is given the negative infinity value, so that there is no chance that the correct multiplier gets skipped.

`with open("monteCarlo-multiplierOptimiser.csv","r") as file:` opens the file, using `with` ensures we don't have to close the file - it closes automatically.
    `datas = csv.reader(file, delimiter=",")` uses the csv module to read the file, stating the delimiter (what seperates the variables) is a comma.
    for eachline in the file:
        `multiplier = float(eachLine[0])` multiplier is the first value
        `score = (float(eachLine[2]) - float(eachLine[1]))` score is the third value - the second value (we want the second value to be lowest, the third to be highest)
        `if score > best_score:` if the score is greater than the current best score:
            `best_score = score` best score is now the current score
            `best_multiplier = multiplier` best multiplier is now the current multipler
`return best_multiplier` gives us the best multiplier

We then define `best_multiplier` as `findOptimum()` - the function

`def doubler_bettor(funds, initial_wager, wager_count, colour):` see: [doubler_bettor](#martingale-strategypy)
`def simple_bettor(funds, initial_wager, wager_count, colour):` see: [simple_bettor](#simple-bettorpy)
`def multiple_bettor(funds, initial_wager, wager_count, colour):` see: [multiple_bettor](#multiplier-optimiserpy)

we then define more variables that are used to set the experiment:
- x is 0, used for the counter - rerunning the experiment each time
- sampleSize, sets the amount of times the experiment reruns 
- startingFunds, wagerSize, wagerCount are all parameters that countrol the bettors

In the next loop we tell the experiment what to do when we run the program
`while True:` - since the program starts until it is stopped (with ctrl + c)
    The busts and profits of each bettor is set to 0.0, allowing a decimal
    The next loop is while the program hasn't run the full length
        we call the functions with the above parameters
        `x+= 1` adds one to x so that the program doesn't run forever
    we then print the bust chances and the profit chances as a percentage
    we then show the graph with labels on its two axis.

## d'Alembert strategy.py

The d'Alembert strategy is very similar to the martingale strategy however, instead of doubling the wager when you lose - they increase it by a set amount. Then, when they win they decrease the wager by a set amount.
## Monte-Carlo grapher.py
## LaBouchere system.py


## Brief

In this Monte-carlo simulation we will attempt to find the "best" gambling strategy, with the highest profit percentage whilst also having the lowest bust rate (where a player loses all their money). In this scenario the player rolls a metaphorical dice with a possible outcome of 1-100, where if the number was 51-99 the player wins. This gives the player a roughly 49% chance of winning.