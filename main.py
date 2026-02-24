import random
import matplotlib 
import matplotlib.pyplot as plt
import time

lower_bust = 31.235
higher_profit = 63.208

sampleSize = 1000
startingFunds = 10000
wagerSize = 100
wagerCount = 100

def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        #print(roll, "roll was 100, you lose - what are the odds? Play again!")
        return False
    elif roll <= 50:
        #print(roll, "roll was 1-50, you lose. Play again!")
        return False

    elif 100 > roll > 50:
        #print(roll, "roll was 51-99, you win!")
        return True

def multiple_bettor(funds, initial_wager, wager_count, colour):
    global multiple_busts
    global multiple_profits
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = "win"
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager ==  "win":
            #print("we won the last wager, great")
            if rollDice():
                value+=wager
                #print(value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = "loss"
                #print(value)
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    #print("we went broke", currentWager, "bets")
                    multiple_busts += 1
                    break

        elif previousWager == "loss":
            #print("Lost the last one, will double")
            if rollDice():
                wager = previousWagerAmount * random_multiple

                if (value - wager) < 0:
                    wager = value
                #print("we won", wager)
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = "win"
                wX.append(currentWager)
                vY.append(value)
            else: 
                wager = previousWagerAmount * random_multiple
                if (value - wager) < 0:
                    wager = value
                #print("we lost", wager)
                value -= wager
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    #print("we went broke after", currentWager, "bets")
                    multiple_busts += 1
                    break

                #print(value)
                previousWager = "loss"



        currentWager += 1

    #print(value)
    #plt.plot(wX,vY, colour)
    if value > funds: 
        multiple_profits += 1

def doubler_bettor(funds, initial_wager, wager_count, colour):
    global doubler_busts
    global doubler_profits
    value = funds
    wager = initial_wager
    wX = []
    vY = []

    currentWager = 1
    previousWager = "win"
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager ==  "win":
            #print("we won the last wager, great")
            if rollDice():
                value+=wager
                #print(value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = "loss"
                #print(value)
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    #print("we went broke", currentWager, "bets")
                    doubler_busts += 1
                    break

        elif previousWager == "loss":
            #print("Lost the last one, will double")
            if rollDice():
                wager = previousWagerAmount * 2

                if (value - wager) < 0:
                    wager = value
                #print("we won", wager)
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = "win"
                wX.append(currentWager)
                vY.append(value)
            else: 
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                #print("we lost", wager)
                value -= wager
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    #print("we went broke after", currentWager, "bets")
                    doubler_busts += 1
                    break

                #print(value)
                previousWager = "loss"



        currentWager += 1

    #print(value)
    plt.plot(wX,vY, colour)
    if value > funds: 
        doubler_profits += 1

def simple_bettor(funds, initial_wager, wager_count, colour):
    global simple_busts
    global simple_profits
    value = funds
    wager = initial_wager
    wX = []
    vY = []

    currentWager = 1

    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

        currentWager += 1

    if value <= 0:
        value = 0
        simple_busts += 1
    #print("funds:", value)

    plt.plot(wX, vY, colour)
    if value > funds: 
        value = 0
        simple_profits += 1

x = 0
while True:
#simple_busts = 0.0
#doubler_busts = 0.0
    multiple_busts = 0.0
#simple_profits = 0.0
#doubler_profits = 0.0
    multiple_profits = 0.0
    multipleSampleSize = 100000
    currentSample = 1

    random_multiple = random.uniform(0.1, 10.0)

    while currentSample <= multipleSampleSize:
        multiple_bettor(startingFunds, wagerSize, wagerCount, "g")
        currentSample += 1
    
    if ((multiple_busts/multipleSampleSize) * 100.00 < lower_bust) and ((multiple_profits/multipleSampleSize)* 100.00 > higher_profit):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("found winner, the multiple was:", random_multiple)
        print("lower bust to beat", lower_bust)
        print("higher profit to beat", higher_profit)
        print("bust rate:", (multiple_busts/multipleSampleSize)* 100.00)
        print("profit rate:", (multiple_profits/multipleSampleSize)* 100.00)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else: 
        pass
        '''print("#########################################################################################")
        print("found loser, the multiple was:", random_multiple)
        print("higher profit to beat", higher_profit)
        print("bust rate:", (multiple_busts/multipleSampleSize)* 100.00)
        print("profit rate:", (multiple_profits/multipleSampleSize)* 100.00)
        print("#########################################################################################")
'''
#while x < sampleSize: # sample size
 #   simple_bettor(startingFunds, wagerSize, wagerCount, "k") # x, x, number of wagers
 #   doubler_bettor(startingFunds, wagerSize, wagerCount, "c") # x, x, number of wagers
'''x+=1

print("Simple bettor bust chance:", (simple_busts/sampleSize) * 100.00)
print("Doubler bettor bust chance:", (doubler_busts/sampleSize) * 100.00)
print("Simple bettor profit chances:", (simple_profits/sampleSize) * 100.00)
print("doubler bettor profit chances:", (doubler_profits/sampleSize) * 100.00)

plt.axhline (0, color = "r")
plt.ylabel("Account Value")
plt.xlabel("wager Count")
plt.show()'''