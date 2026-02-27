import random
import matplotlib 
import matplotlib.pyplot as plt

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
    
def doubler_bettor(funds, initial_wager, wager_count):
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
                    wX.append(currentWager)
                    vY.append(value)
                    #print("we went broke after", currentWager, "bets")
                    doubler_busts += 1
                    break

        elif previousWager == "loss":
            #print("Lost the last one,so we will be smart and double")
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
                    wX.append(currentWager)
                    vY.append(value)
                    doubler_busts += 1
                    break
                #print(value)
                previousWager = "loss"
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
        currentWager += 1
    #print(value)
    plt.plot(wX,vY)
    if value > funds: 
        doubler_profits += 1

x = 0
sampleSize = 1000 # if you only want one example, set to 1
startingFunds = 100000

wagerSize = 100
wagerCount = 100

while True:
    doubler_busts = 0.0
    doubler_profits = 0.0

    while x < sampleSize: # sample size
        doubler_bettor(startingFunds, wagerSize, wagerCount)
        x+=1

    print("Doubler bettor bust chance:", (doubler_busts/sampleSize) * 100.00)
    print("doubler bettor profit chances:", (doubler_profits/sampleSize) * 100.00)

    plt.axhline (0, color = "r")
    plt.ylabel("Account Value")
    plt.xlabel("wager Count")
    plt.show()