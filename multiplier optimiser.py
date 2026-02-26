# optimise multiplier
import random

lower_bust = 31.235
higher_profit = 63.208

startingFunds = 100000
wagerSize = 100
wagerCount = 100000


def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False


    elif roll <= 50: #50/50 odds
        #print(roll, "roll was 1-50, you lose. Play again!")
        return False

    elif 100 > roll > 50:
        #print(roll, "roll was 51-99, you win!")
        return True

def multiple_bettor(funds, initial_wager, wager_count):
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

while True:

    multiple_busts = 0.0
    multiple_profits = 0.0
    multipleSampleSize = 100000
    currentSample = 1

    random_multiple = random.uniform(0.1, 10.0)

    while currentSample <= multipleSampleSize:
        multiple_bettor(startingFunds, wagerSize, wagerCount)
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