import random

def rollDice(): #50/50 odds
    roll = random.randint(1,100)

    if roll <= 50: 
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

        saveFile = open("monteCarlo-dAlembert.csv", "a")
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

        saveFile = open("monteCarlo-dAlembert.csv", "a")
        saveLine = "\n" + str(percentROI) + "," + str(wagerSizePercent)+ "," + str(wagerCount)+ ",r"
        saveFile.write(saveLine)
        saveFile.close()