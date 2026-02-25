import random
import matplotlib 
import matplotlib.pyplot as plt
import time

def rollDice():
    roll = random.randint(1,100)

    if roll <= 50: #50/50 odds
        #print(roll, "roll was 1-50, you lose. Play again!")
        return False

    elif roll >= 51:
        #print(roll, "roll was 51-99, you win!")
        return True

def dAlembert(funds, initial_wager, wager_count):
    global Ret #return
    global da_busts # 
    global da_profits

    value = funds
    wager = initial_wager
    currentWager = 1
    previousWager = "win"
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == "win":
            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager

            #print("current wager:", wager, "value:", value)

            if rollDice():
                value += wager
                #print("we won, current value:", value)
                previousWagerAmount = wager
            else:
                value -= wager
                previousWager = "loss"
                #print("we lost, current value:", value)
                previousWagerAmount = wager

                if value <= 0:
                    da_busts += 1
                    break

        elif previousWager == "loss":
            wager = previousWagerAmount + initial_wager
            if (value - wager) <= 0:
                wager = value
            #print("we lost the last wager, current wager:", wager, "value:", value )

            if rollDice():
                value += wager
                #print("we won, current value:", value)
                previousWagerAmount = wager
                previousWager = "win"

            else:
                value -= wager
                #print("we lost, current value:", value)
                previousWagerAmount = wager

                if value <= 0:
                    da_busts += 1
                    break

        currentWager += 1

    if value > funds:
        da_profits += 1

    #print(value)

    Ret += value


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

random_multiple = random.uniform(0.1, 10.0)
x = 0
lower_bust = 31.235
higher_profit = 63.208


sampleSize = 1000
startingFunds = 100000

while True:

    #wagerSize = 100
    #wagerCount = 100000
    wagerSize = random.uniform(1.0, 1000.00)
    wagerCount = random.uniform(10.0, 10000)

    Ret = 0.0
    da_busts = 0.0
    da_profits = 0.0
    daSampSize = 10000
    counter = 1

    while counter <= daSampSize:
        dAlembert(startingFunds, wagerSize, wagerCount)
        counter += 1

    ROI = Ret - (daSampSize* startingFunds)
    totalInvested = daSampSize*startingFunds

    percentROI = (ROI/totalInvested) * 100.00
    wagerSizePercent = (wagerSize/startingFunds) * 100.00

    if percentROI > 1:
        print("_________________________________________________________")
        print("percent ROI:", percentROI)
        print("total invested:", daSampSize* startingFunds)
        print("total return:", Ret)
        print("ROI", Ret - (daSampSize* startingFunds))
        print("bust rate", (da_busts/daSampSize)* 100.00)
        print("profit rate", (da_profits/daSampSize)* 100.00)
        print("wager size:", wagerSize)
        print("wager count:", wagerCount)
        print("wager size percentage:", (wagerSize/startingFunds)*100)

        saveFile = open("monteCarloLiberal.csv", "a")
        saveLine = "\n" + str(percentROI) + "," + str(wagerSizePercent)+ "," + str(wagerCount)+ ",g"
        saveFile.write(saveLine)
        saveFile.close()

    elif percentROI > -1:
        print("_________________________________________________________")
        print("percent ROI:", percentROI)
        print("total invested:", daSampSize* startingFunds)
        print("total return:", Ret)
        print("ROI", Ret - (daSampSize* startingFunds))
        print("bust rate", (da_busts/daSampSize)* 100.00)
        print("profit rate", (da_profits/daSampSize)* 100.00)
        print("wager size:", wagerSize)
        print("wager count:", wagerCount)
        print("wager size percentage:", (wagerSize/startingFunds)*100)

        saveFile = open("monteCarloLiberal.csv", "a")
        saveLine = "\n" + str(percentROI) + "," + str(wagerSizePercent)+ "," + str(wagerCount)+ ",r"
        saveFile.write(saveLine)
        saveFile.close()
'''
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
        print("#########################################################################################")
        print("found loser, the multiple was:", random_multiple)
        print("higher profit to beat", higher_profit)
        print("bust rate:", (multiple_busts/multipleSampleSize)* 100.00)
        print("profit rate:", (multiple_profits/multipleSampleSize)* 100.00)
        print("#########################################################################################")

#while x < sampleSize: # sample size
 #   simple_bettor(startingFunds, wagerSize, wagerCount, "k") # x, x, number of wagers
 #   doubler_bettor(startingFunds, wagerSize, wagerCount, "c") # x, x, number of wagers
x+=1


print("Simple bettor bust chance:", (simple_busts/sampleSize) * 100.00)
print("Doubler bettor bust chance:", (doubler_busts/sampleSize) * 100.00)
print("Simple bettor profit chances:", (simple_profits/sampleSize) * 100.00)
print("doubler bettor profit chances:", (doubler_profits/sampleSize) * 100.00)

plt.axhline (0, color = "r")
plt.ylabel("Account Value")
plt.xlabel("wager Count")
plt.show()
'''