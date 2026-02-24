import random
import matplotlib 
import matplotlib.pyplot as plt
import time

sampleSize = 1000
startingFunds = 10000
wagerSize = 100
wagerCount = 1000

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
'''
def doubler_bettor(funds, initial_wager, wager_count, colour):
    value = funds
    wager = initial_wager
    global doubler_busts
    global doubler_profits
    wX = []
    vY = []

    currentWager = 1
    previousWager = "win"
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == "win":
            #print("we won the last one")
            if rollDice():
                value += wager
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
                    #print("we went broke after", currentWager, "bets")
                    doubler_busts += 1
                    break

        elif previousWager == "loss":
            #print("we lost the last one, so will double it")
            if rollDice():
                wager = previousWagerAmount * 2

                #if( value - wager) > 0: 
                if value > wager:
                    wager = value
                print("we won", wager)
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = "win"
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2

                #if(value - wager) > 0:
                if value > wager: 
                    wager = value
                print("we lost", wager)
                value -= wager
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    print("we went broke after", currentWager, "bets")
                    doubler_busts += 1
                    break

                #print(value)
                previousWager = "loss"

        currentWager += 1

    #print(value)
    plt.plot(wX, vY, colour)
    if value > funds: 
        doubler_profits += 1
'''
def doubler_bettor(funds, initial_wager, wager_count, colour):
    global simple_busts
    global simple_profits
    value = funds
    wager = initial_wager
    global broke_count
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
                    broke_count += 1
                    break

        elif previousWager == "loss":
            #print("Lost the last one, will double")
            if rollDice():
                wager = previousWagerAmount * 2
                #print("we won", wager)
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = "win"
                wX.append(currentWager)
                vY.append(value)
            else: 
                wager = previousWagerAmount * 2
                #print("we lost", wager)
                value -= wager
                if value < 0:
                    #print("we went broke after", currentWager, "bets")
                    broke_count += 1
                    break

                #print(value)
                previousWager = "loss"

                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

        currentWager += 1

    #print(value)
    plt.plot(wX,vY)

'''xx = 0
broke_count = 0

while xx < 1000:
    doubler_bettor(10000, 100, 100, "r")
    xx+=1

print("death rate", (broke_count/float(xx))* 100)
print("survival rate:", 100 - (broke_count/float(xx))* 100)

plt.axhline (0, color = "r")
plt.show()

'''


def simple_bettor(funds, initial_wager, wager_count, colour):
    global simple_busts
    global simple_profits
    value = funds
    wager = initial_wager
    global broke_count
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
        broke_count += 1
        simple_busts += 1
    #print("funds:", value)

    plt.plot(wX, vY, colour)
    if value > funds: 
        #value = 0
        simple_profits += 1

x = 0
broke_count = 0
simple_busts = 0.0
doubler_busts = 0.0
simple_profits = 0.0
doubler_profits = 0.0

while x < sampleSize: # sample size
    simple_bettor(startingFunds, wagerSize, wagerCount, "k") # x, x, number of wagers
    #doubler_bettor(startingFunds, wagerSize, wagerCount, "c") # x, x, number of wagers
    x+=1
print("death rate", (broke_count/float(x))* 100)
print("survival rate:", 100 - (broke_count/float(x))* 100)
print("Simple bettor bust chance:", (simple_busts/sampleSize) * 100.00)
print("Doubler bettor bust chance:", (doubler_busts/sampleSize) * 100.00)

print("Simple bettor profit chances:", (simple_profits/sampleSize) * 100.00)
print("doubler bettor profit chances:", (doubler_profits/sampleSize) * 100.00)

plt.axhline (0, color = "r")
plt.ylabel("Account Value")
plt.xlabel("wager Count")
plt.show()