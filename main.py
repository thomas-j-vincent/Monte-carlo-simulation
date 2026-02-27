import random
import matplotlib 
import matplotlib.pyplot as plt
import csv

def rollDice():
    roll = random.randint(1,100)
    if roll == 100:
        #print(roll, "roll was 100, womp, womp")
        return False

    elif roll <= 50: #50/50 odds
        #print(roll, "roll was 1-50, you lose. Play again!")
        return False

    elif 100 >roll > 50:
        #print(roll, "roll was 51-99, you win!")
        return True

def findOptimum():

    best_multiplier = None
    best_score = float('-inf')

    with open("monteCarlo-multiplierOptimiser.csv","r") as file:
        datas = csv.reader(file, delimiter=",")
        for eachLine in datas:
            multiplier = float(eachLine[0])
            score = (float(eachLine[2]) - float(eachLine[1]))

            if score > best_score:
                best_score = score
                best_multiplier = multiplier
    
    return best_multiplier

best_multiplier = findOptimum()

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

    currentWager = 1 # ???

    while currentWager <= wager_count: # ??
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
            if rollDice():
                value+=wager
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                wX.append(currentWager)
                vY.append(value)
                previousWager = "loss"
                previousWagerAmount = wager
                if value < 0:
                    multiple_busts += 1
                    break

        elif previousWager == "loss":
            if rollDice():
                wager = previousWagerAmount * best_multiplier

                if (value - wager) < 0:
                    wager = value
                value += wager
                wX.append(currentWager)
                vY.append(value)
                wager = initial_wager
                previousWager = "win"
            else: 
                wager = previousWagerAmount * best_multiplier
                if (value - wager) < 0:
                    wager = value
                value -= wager
                wX.append(currentWager)
                vY.append(value)
                previousWagerAmount = wager
                if value <= 0:
                    multiple_busts += 1
                    break

                previousWager = "loss"

        currentWager += 1
    plt.plot(wX, vY)
    if value > funds: 
        multiple_profits += 1

x = 0

sampleSize = 1000
startingFunds = 100000
wagerSize = 100
wagerCount = 100

while True:
    simple_busts = 0.0
    doubler_busts = 0.0
    multiple_busts = 0.0
    simple_profits = 0.0
    doubler_profits = 0.0
    multiple_profits = 0.0
    

    while x < sampleSize: # sample size
        simple_bettor(startingFunds, wagerSize, wagerCount, "k") # x, x, number of wagers
        doubler_bettor(startingFunds, wagerSize, wagerCount, "c") # x, x, number of wagers
        multiple_bettor(startingFunds, wagerSize, wagerCount, "y") # x, x, number of wagers
        x+=1


    print("Simple bettor bust chance:", (simple_busts/sampleSize) * 100.00)
    print("Doubler bettor bust chance:", (doubler_busts/sampleSize) * 100.00)
    print("Multiple bettor bust chance:", (multiple_busts/sampleSize) * 100.00)
    print("Simple bettor profit chances:", (simple_profits/sampleSize) * 100.00)
    print("doubler bettor profit chances:", (doubler_profits/sampleSize) * 100.00)
    print("Multiple bettor profit chances:", (multiple_profits/sampleSize) * 100.00)

    plt.axhline (0, color = "r")
    plt.ylabel("Account Value")
    plt.xlabel("wager Count")
    plt.show()