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
    
def simple_bettor(funds, initial_wager, wager_count):
    global simple_busts
    global simple_profits
    value = funds
    wager = initial_wager
    wX = []
    vY = []

    currentWager = 0 # ???

    while currentWager <= wager_count: # How many wagers each bettor places
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

    plt.plot(wX, vY)
    if value > funds: 
        value = 0
        simple_profits += 1

x = 0

sampleSize = 1000
startingFunds = 100000

wagerSize = 100
wagerCount = 100000

while True:
    simple_busts = 0.0
    simple_profits = 0.0
    

    while x < sampleSize: # sample size
        simple_bettor(startingFunds, wagerSize, wagerCount) # x, x, number of wagers
        x+=1

    print("Simple bettor bust chance:", (simple_busts/sampleSize) * 100.00)
    print("Simple bettor profit chances:", (simple_profits/sampleSize) * 100.00)

    plt.ylabel("Account Value")
    plt.xlabel("wager Count")
    plt.show()