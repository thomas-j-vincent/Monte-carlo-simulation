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
filename = "monteCarlo-multiplierOptimiser.csv"
#filename = "monteCarlo-dAlembert.csv"

def graph():
    with open(filename,"r") as montecarlo:
        datas = csv.reader(montecarlo, delimiter=",")

        for eachLine in datas:
            percentROI = float(eachLine[0])
            wagerSizePercent = float(eachLine[1])
            wagerCount = float(eachLine[2])
            pcolor = eachLine[3]

            ax.scatter(wagerSizePercent,wagerCount,percentROI,color=pcolor)

            if filename == "monteCarlo-dAlembert.csv":
                ax.set_xlabel("wager percent size")
                ax.set_ylabel("wager count")
                ax.set_zlabel("percent ROI")

            elif filename == "monteCarlo-multiplierOptimiser.csv":
                ax.set_xlabel("multiple")
                ax.set_ylabel("bust rate")
                ax.set_zlabel("profit rate")

    plt.show()

graph()
