# Monte-carlo-simulation

The Monte-carlo simulation is a method of predicting outcomes using random numbers by running numerous simulations and taking a mean of the results, the main concept being using randomness to solve deterministic problems(problems where no randomness is involved). It is used to "brute-force" solutions to problems too complex to solve via mathematical analysis, under the topics; optimisation, numerical integration and probability distribution such as the number of Pi. Another usecase is to determine the risk of a strategy, such as trading or gambling as the monte carlo simulation can run through many possible outcomes and calculate the probability of one being the outcome that you want.
## Contents:  

- [Simple bettor](#simple-bettorpy) 
- [Martingale strategy](#martingale-strategypy)
- [Multiplier optimiser](#multiplier-optimiserpy)
- [Main.py](#main.py) 
- [D'Alembert strategy](#Dalembert-strategypy)
- [LaBouchere system](#labouchere-systempy)
- [Monter-carlo grapher](#monte-carlo-grapherpy)

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
- startingFunds, wagerSize, wagerCount are all parameters that countrol the bettor

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

The function multiplier_bettor takes three parameters: `funds, initial_wager, wager_count`
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
- startingFunds, wagerSize, wagerCount are all parameters that countrol the bettor

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

Main.py is used to compare the three multiplier-based betting strategies, and returns its busts and profits per sample size. The image below shows the graphical output of the program - excluding the busts and profits which are printed to the terminal. In this image simple bettor is in black, double bettor is in blue, multiple bettor is in red and D'Alembert's bettor is in green. As you can see the double bettor, the multiple bettor and D'Alembert's bettor result in aproximately the same profits; but the multiple bettor often recovers more quickly - reducing its chances of going broke And D'Alembert's bettor often falls not as much at all
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
`def dAlembert(funds, initial_wager, wager_count):` see: [D'Alembert strategy](#Dalembert-strategy)

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

## D'Alembert strategy.py

The D'Alembert strategy is very similar to the martingale strategy however, instead of doubling the wager when you lose - they increase it by a set amount. Then, when they win they decrease the wager by a set amount until it reaches its original wager.

### code

We import only one module this time: 
- Random, which is used to act as a dice to pick a number from 1- 100

The function rollDice is the dice function, and has three outcomes: if roll is 100, the player loses and the function returns false, if the roll is less than or equal to 50, the player loses and the function returns false, and if the number is less than 100 but larger than 50 the player wins and the function returns true. Giving a 49% chance of winning.

The function multiplier_bettor takes three parameters: `funds, initial_wager, wager_count`
- funds is the starting amount that each bettor starts out with
- initial_wager is the amount the bettors are permitted to bet each round
- wager_count is the amount of bets they are allowed to place


We start off creating a few variables, `global ret`, `global da_busts` and `global da_profits` which are used to track how many times the bettors go broke or make a profit (these values are returned at the end of the program). 
`value` is set as the `funds`, so we can take away or add on winning or losing bets to return a final value
`wager` is set as `initial_wager`, the wager we will place each time.
`currentWager` is set at 1, but could just as easily be 0.
`previousWager` is set as `"win"` This is needed as it depends on the previous outcome whether the bettor increases the wager or not.
`previousWagerAmount` is set as `initial_wager`, also required because you are not just increasing the initial wager - it could have happened more than once.

We then enter the main portion of the function: 
`while currentWager <= wager_count:` means that for the amount of wagers each bettor has to place
    `if previousWager` is `"win"` if the bettor won the last bet
        `if wager == initialWager:` if the wager is already the lowest it can be,
            `pass` skip
        `else` if the wager is not the lowest it can be
            `wager -= initial_wager` subtract one unit from the wager
        `if rollDice():` is true:
            `value += wager`we add the wager value to the overall value (as profit)
            `previousWagerAmount = wager` we set the previous wager, so we know what to increase/decrease
        `else:` if roll dice is false (the bettor has lost the bet)
            `value -= wager`we subtract the wager value from the overall value (as loss)
            `previousWager = "loss"` we set the previous wager to loss so that we know to increase the bet next time.
            `previousWagerAmount = "wager"` we set the previous wager, so we know what to increase/decrease
            `if value <= 0:` if the bettor has lost all their money and has gone broke
            `da_busts += 1` add one to D'Alembert busts (returned later)
            `break` go back to the start 
    `elif previousWager == "loss"` if the bettor lost the last bet
        `wager = previousWagerAmount + initial_wager` increase the wager by a wager (one unit) - and set it as the current wager
        `if (value - wager) < 0:` if the current wager is larger than the money the bettor has left
        `wager = value` set the wager to all the money we have left instead
        `if rollDice():` is true:
            `value += wager` add the wager to the value, so we know what we have left
            `previousWagerAmount = "initial_wager"` as we have won, we reset to the original wager
            `previousWager = "win"` we set the previous wager so we know there is no need to double
        `else:` if the bettor loses =:
            `value -= wager` subtract the wager from the value, so we know what we have left
            `previousWagerAmount = wager` we set the previous wager so we know what to double - or not - next.
            `if value <= 0:` if the bettor has lost all their money and has gone broke
                `da_busts += 1` add one to D'Alembert busts (returned later)
                `break` go back to the start
    `currentWager += 1` add one to currentWager, the bettor has successfully placed a bet
`if value > funds:` if the value is greater than original funds
    `da_profits += 1` add one to the profit counter
`Ret += value`

we then define more variables that are used to set the experiment:
- sampleSize, sets the amount of times the experiment reruns 
- startingFunds, is a parameter that countrols the bettor

In the next loop we tell the experiment what to do when we run the program
`while True:` - since the program starts until it is stopped (with ctrl + c)
    `wagerSize = random.uniform(1.0, 1000.00)` wager size is a random number from 1.0 - 1000.00
    `wagerCount = random.uniform(10.0, 100000)` wager count is a random number from 10.0 - 100000
    `Ret` is set as 0.0, (the money made from this bettor with these random numbers)
    `da_busts` and `da_profits` are set to 0.0, allowing a decimal
    `daSampleSize` is set to a number which is passed to the function
    `counter` is the incremental value, set here to 1 but could just as easily be 0
    The next loop is while the program hasn't run the full length
        `multiple_bettor(startingFunds, wagerSize, wagerCount)` calls the function with the above parameters
        `dAlembert+= 1` adds one to x so that the program doesn't run forever
    `ROI` is calculated as `Ret - (daSampSize* startingFunds)`, 
    `totalInvested` is the sample size multiplied by the starting funds
    `percentROI` is the `ROI` divided by `totalInvested` multiplied by `100.00`
    `wagerSizePercent` is the `wagerSize` divided by the `startingFunds` multiplied by `100.00`
    Then if the ROI as a percentage is greater than 1 (we make money) we:
        print out all the variables,
        we open the file `monteCarlo-dAlembert.csv`
        and then create a line with `percentROI`, `wagerSizePercent` and `wagerCount` in the colour green
        and then close the file
    If the percent ROI is less than one (we lost money) we:
        print out all the variables,
        we open the file `monteCarlo-dAlembert.csv`
        and then create a line with `percentROI`, `wagerSizePercent` and `wagerCount` in the colour red (for loss)
        and then close the file

## LaBouchere system.py

The LaBouchere system is a progressive betting system where you set a predefined amount of money you want to win beforehand, you then select some wagers that in turn add up to your selected "win" amount, the more wagers the safer each one will be - but also the longer it will take. In this program we used 10 wagers of 1, but another example would be 5 wagers of: 1, 2, 2, 3, 2. you then wager the first number plus the last number - so in the example we used in the program it would be 2- these numbers are then removed from the list. If you lose you add the wager to the end of the list, so that the next wager wouls be 1 + (1+1) which is 3. This continues until all of the numbers are gone. The overall aim is that you do not have to win all the time to win the predetermined amount of money. 

### Code 

We import three modules: 
- Random, which is used to act as a dice to pick a number from 1- 100
- Matplotlib; which is used for plotting the graph
- Pyplot; which is the specific graph that we use
- style; which allows us to format the graph in two halves

`style.use("ggplot")` sets the graph style ro have a grey background with white grid lines

We then define some variables, all zero:`broke_count, totalFunded, totalEnding, wins, losses`

The function itself requires no parameters
    we then global the variables we declared just above the function
    we set some more variables: `starting_funds = 100`, `totalFunded` equal `starting_funds` but gets the profits added to it, `goal` is the intended amount of money we make, here it is 10 units. `system` is the way we have chosen to lay out our wagers - here it is `[1,1,1,1,1,1,1,1,1,1]`. `profit` is set as 0 to begin with, `current_funds` equal starting funds but will gradually be increased or decreased depending on the money left over. `wagerSizes = []` and `plot_funds = []` is where the points for the graph will be passed. 
    Finally we set `not_broke` as `True` as we are currently not broke.
`
    We then enter the main body of the function:
    `while profit < goal and not_broke:` whilst our profit is less than our goal and we have not run out of money
        `if len(system) > 1:` If the amount of numbers in our system (betting plan) is larger than one and we therefore have to do some addition
            `size = system[0] + system[-1]` The size of the wager is the size of the first and last numbers of the system
            `wagerSizes.append(size)` add this number to the list `wagerSizes`
            `plot_funds.append(current_funds)` add `current_funds` to the list `plot_funds` to be graphed later
        `
        `else:`  if there is only one number left:
            `size = system[0]` Use the final number left as the size of the wager
            `wagerSizes.append(size)` add this number to the list `wagerSizes`
            `plot_funds.append(current_funds)`  add `current_funds` to the list `plot_funds` to be graphed later
`
        `if current_funds <=0:` if `current_funds` is less than or equal to 0
            `not_broke = False` change `not_broke` to `False` (as we are broke now)
            `broke_count += 1` add 1 to the broke count
            `losses += 1` add 1 to the losses
`
        `elif current_funds - size <= 0:` if `current_funds` - the wager size is less than or equal to 0: 
            `size = current_funds` the size is the amount of money left
            `not_broke = False` set `not_broke` to `False` (as we are broke now)
            `broke_count += 1` add 1 to the broke count
            `losses += 1` add 1 to the losses
`
        `dice = random.randrange(1,101)` dice is a random roll from 1-100 - the variable does not contain the last number.
        `if dice < 51:` if the dice roll is less than 51
            `losses += 1` add 1 to the losses 
            `system.append(size)` add the size to the system - we lost so add it on to the end
            `current_funds -= size` subtract the size from the `current_funds` (as we lost that money)
            `profit = current_funds - starting_funds` profit is the funds left - the starting funds
`
        `else:` if the dice roll is greater than 50
            `wins += 1` add one to the wins
            `current_funds += size` add the size to the `current_funds`
            `profit = current_funds - starting_funds` profit is the funds left - the starting funds
            `if profit != goal:` if profit is not the the goal:
                `try:` try to:
                    `del system[0]` delete the first and last number of the system list
                    `del system[-1]`
                `except:` otherwise 
                    `pass` skip
`
    `wagerSizes.append(size)`  add th size to the list `wagerSizes`
    `plot_funds.append(current_funds)` add the final`current_funds` to the list `plot_funds` to be graphed later
    `totalEnding += current_funds` add `current_funds` to the total ending, so we know how much money we had at the end
    `s1.plot(wagerSizes)` plot `wagerSizes` in the first graph
    `s2.plot(plot_funds)` and `plot_funds` in the second graph

`f = plt.figure()` creates a new figure in the plot
`s1 = f.add_subplot(211)` add s1 to the figure - with 2 rows, 1 column, at position 1
`s2 = f.add_subplot(212)` add s2 to the figure - with 2 rows, 1 column, at position 2

`sample_size = 1000` sets the sample size at 1000
`for x in range(sample_size):` calls the function until it has been called the number of sample size times
    `Labouchere()`

At the end we print the start amount, and then the end amount. Along with the amount of times the bettors went broke as a percentage, multiplied by 100.

We then show the graph.

## Monte-Carlo grapher.py

The grapher takes any files that can be interpreted as 3d charts and creates one, we currently have the multiplier optimiser (helping to see the relationship between the multiple to the profit and bust rate) and the D'Alembert strategy (helping to show the relationship between the ROI to the wager size and the wager count)

### Code

We first import three modules
- Matplotlib; which is used for plotting the graph
- Pyplot; which is the specific graph that we use
- csv; which helps us to read the strategy files
- mplot3d; which allows the graph to be 3D

`fig = plt.figure()` we first create a figure
`ax = fig.add_subplot(111, projection="3d")` we add an axis with one row, one column at position one, with a 3D projection
``` python
filename = "monteCarlo-multiplierOptimiser.csv"
#filename = "monteCarlo-dAlembert.csv"
``` 
are options for the filename (which file gets read)

`with open("monteCarlo-multiplierOptimiser.csv","r") as montecarlo:` opens the file, using `with` ensures we don't have to close the file - it closes automatically.
    `datas = csv.reader(montecarlo, delimiter=",")` uses the csv module to read the file, stating the delimiter (what seperates the variables) is a comma.
    for eachline in the file:
        `percentROI = float(eachLine[0])` ROI is the first value
        `wagerSizePercent = float(eachLine[1])` wager size as a percentage is the second value
        `wagerCount = float(eachLine[2])` wager count it the third value
        `pcolor = eachLine[3]` colour is the last variable    
        `ax.scatter(wagerSizePercent,wagerCount,percentROI,color=pcolor)` plots the data on the graph
        if the file name is `"monteCarlo-dAlembert.csv"`:
            the x axis label is `wager percent size`
            the y axis label is `wager count`
            the z axis label is `percent ROI`
        otherwise if the filename is `monteCarlo-multiplierOptimiser.csv`:
            the x axis label is `multiple`
            the y axis label is `bust rate`
            the z axis label is `profit rate`
`plt.show()` show the graph 

`graph()` calls the graphing function
