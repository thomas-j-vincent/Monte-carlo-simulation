'''
Takes the csv files generated from the monte-carlo models and graphs them to a 3d chart, 
just uncomment the line with the file you want to read from and comment out the others
'''

import matplotlib
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

def graph():
    #with open("monteCarloLiberal.csv","r") as montecarlo:
    #with open("monteCarloLiberal.csv","r") as montecarlo:
    with open("monteCarlo-dAlembert.csv","r") as montecarlo:
        datas = csv.reader(montecarlo, delimiter=",")

        for eachLine in datas:
            percentROI = float(eachLine[0])
            wagerSizePercent = float(eachLine[1])
            wagerCount = float(eachLine[2])
            pcolor = eachLine[3]

            ax.scatter(wagerSizePercent,wagerCount,percentROI,color=pcolor)

            ax.set_xlabel("wager percent size")
            ax.set_ylabel("wager count")
            ax.set_zlabel("percent ROI")

    plt.show()

graph()
