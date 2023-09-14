import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as wplt

def calculateUnityCut(copiesSold):
    price1 = 0.2
    price2 = 0.2
    price3 = 0.2
    price4 = 0.2

    cut = 0

    if (copiesSold < 200000):
        return cut

    copiesSold -= 200000

    if (copiesSold < 100000):
        cut += copiesSold * price1
        return cut
    else:
        cut += 100000 * price1
    
    copiesSold -= 100000

    if (copiesSold < 400000):
        cut += copiesSold * price2
        return cut
    else:
        cut += 400000 * price2

    copiesSold -= 400000

    if (copiesSold < 500000):
        cut += copiesSold * price3
        return cut
    else:
        cut += 500000 * price3
    
    copiesSold -= 500000

    cut += copiesSold * price4
    return cut

def calculateUnityProCut(copiesSold):
    price1 = 0.15
    price2 = 0.08
    price3 = 0.03
    price4 = 0.02

    cut = 0

    if (copiesSold < 200000):
        return cut

    copiesSold -= 200000

    if (copiesSold < 100000):
        cut += copiesSold * price1
        return cut
    else:
        cut += 100000 * price1
    
    copiesSold -= 100000

    if (copiesSold < 400000):
        cut += copiesSold * price2
        return cut
    else:
        cut += 400000 * price2

    copiesSold -= 400000

    if (copiesSold < 500000):
        cut += copiesSold * price3
        return cut
    else:
        cut += 500000 * price3
    
    copiesSold -= 500000

    cut += copiesSold * price4
    return cut

def calculateEpicCut(copiesSold, gamePrice):
    return copiesSold * gamePrice * 0.05

def calculateGodotCut(copiesSold, gamePrice):
    return 0

def calculateSteamCut(copiesSold, gamePrice):
    return copiesSold * gamePrice * 0.3

minimumWageFunction = lambda x: 31000
targetWageFunction = lambda x: 31000

devs = 3
pricePerGame = 5
downloadsPerGame = 5

minXValue = 0
maxXValue = 1000000
step = 1000

x = np.arange(minXValue, maxXValue, step)

unityEarnings = np.array([(i * pricePerGame * 0.7 - calculateUnityCut(i * downloadsPerGame)) / devs for i in x])
unityPlusEarnings = np.array([(i * pricePerGame * 0.7 - calculateUnityProCut(i * downloadsPerGame)) / devs - (devs * 2040) for i in x])
epicEarnings = np.array([(i * pricePerGame * 0.7 - calculateEpicCut(i, pricePerGame)) / devs for i in x])
godotEarnings = np.array([(i * pricePerGame * 0.7) / devs for i in x])

minimumWage = np.array([minimumWageFunction(i) for i in x])

plt.plot(x, unityEarnings, label="Unity")
plt.plot(x, unityPlusEarnings, label="Unity Plus")
plt.plot(x, epicEarnings, label="Epic")
plt.plot(x, godotEarnings, label="Godot (any free engine)")
plt.plot(x, minimumWage, label="Minimum wage", linestyle="dashed")

plt.xlabel("Sales")
plt.ylabel("Earnings per developer")

plt.legend()

plt.title(f"Earnings per developer for different engines ({devs}: devs, {downloadsPerGame}: average downloads per buy, ${pricePerGame}USD: price per copy)")

# add grid
plt.grid(which='both')
plt.grid(which='major',alpha=.4,linestyle='--')
plt.grid(which='minor',alpha=.1,linestyle='--')

minYValues = [min(unityEarnings), min(unityPlusEarnings), min(epicEarnings), min(godotEarnings), min(minimumWage)]
maxYValues = [max(unityEarnings), max(unityPlusEarnings), max(epicEarnings), max(godotEarnings), max(minimumWage)]

plt.xticks(np.arange(minXValue, maxXValue, step * 10), minor=True)
plt.xticks(np.arange(minXValue, maxXValue, step * 100))
plt.yticks(np.arange(min(minYValues), max(maxYValues), step * 10), minor=True)

plt.show()