import random

print("starting...")

lower_bust = 31.235
higher_profit = 63.208

startingFunds = 100000
wagerSize = 100
wagerCount = 100


def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False

    elif roll <= 50: #50/50 odds
        return False

    elif 100 > roll > 50:
        return True

def multiple_bettor(funds, initial_wager, wager_count):
    global multiple_busts
    global multiple_profits

    value = funds
    wager = initial_wager

    currentWager = 1
    previousWager = "win"
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager ==  "win":
            if rollDice():
                value+=wager
            else:
                value -= wager
                previousWager = "loss"
                previousWagerAmount = wager
                if value < 0:
                    multiple_busts += 1
                    break

        elif previousWager == "loss":
            if rollDice():
                wager = previousWagerAmount * random_multiple

                if (value - wager) < 0:
                    wager = value
                value += wager
                wager = initial_wager
                previousWager = "win"
            else: 
                wager = previousWagerAmount * random_multiple
                if (value - wager) < 0:
                    wager = value
                value -= wager
                previousWagerAmount = wager
                if value <= 0:
                    multiple_busts += 1
                    break

                previousWager = "loss"

        currentWager += 1

    if value > funds: 
        multiple_profits += 1

while True:

    multiple_busts = 0.0
    multiple_profits = 0.0
    multipleSampleSize = 10000
    currentSample = 1

    random_multiple = random.uniform(0.1, 10.0)

    while currentSample <= multipleSampleSize:
        multiple_bettor(startingFunds, wagerSize, wagerCount)
        currentSample += 1

    if ((multiple_busts/multipleSampleSize) * 100.00 < lower_bust) and ((multiple_profits/multipleSampleSize)* 100.00 > higher_profit):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        profit_rate = (multiple_profits/multipleSampleSize)* 100.00
        bust_rate = (multiple_busts/multipleSampleSize)* 100.00
        print("found winner, the multiple was:", random_multiple)
        print("lower bust to beat", lower_bust, "this rate:", bust_rate)
        print("higher profit to beat", higher_profit, "this rate:", profit_rate)
        saveFile = open("monteCarlo-multiplierOptimiser.csv", "a")
        saveLine = "\n" + str(random_multiple) + "," + str(bust_rate)+ "," + str(profit_rate)+ ",g"
        saveFile.write(saveLine)
        saveFile.close()
    else: 
        pass
        profit_rate = (multiple_profits/multipleSampleSize)* 100.00
        bust_rate = (multiple_busts/multipleSampleSize)* 100.00
        if (bust_rate or profit_rate) != (100.00 or 0.0):
            saveFile = open("monteCarlo-multiplierOptimiser.csv", "a")
            saveLine = "\n" + str(random_multiple) + "," + str(bust_rate)+ "," + str(profit_rate)+ ",r"
            saveFile.write(saveLine)
            saveFile.close()