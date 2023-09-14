import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as wplt

def calculateUnityCut(copiesSold, pricePerGame, DownloadsPerGame):
    price1 = 0.2
    price2 = 0.2
    price3 = 0.2
    price4 = 0.2

    cut = 0

    copiesDownloaded = copiesSold * DownloadsPerGame

    if (copiesDownloaded < 200000 or copiesSold * pricePerGame < 200000):
        return cut

    copiesDownloaded -= 200000

    if (copiesDownloaded < 100000):
        cut += copiesDownloaded * price1
        return cut
    else:
        cut += 100000 * price1
    
    copiesDownloaded -= 100000

    if (copiesDownloaded < 400000):
        cut += copiesDownloaded * price2
        return cut
    else:
        cut += 400000 * price2

    copiesDownloaded -= 400000

    if (copiesDownloaded < 500000):
        cut += copiesDownloaded * price3
        return cut
    else:
        cut += 500000 * price3
    
    copiesDownloaded -= 500000

    cut += copiesDownloaded * price4
    return cut

def calculateUnityProCut(copiesSold, pricePerGame, DownloadsPerGame):
    price1 = 0.15
    price2 = 0.08
    price3 = 0.03
    price4 = 0.02

    cut = 0

    copiesDownloaded = copiesSold * DownloadsPerGame

    if (copiesDownloaded < 1000000 or copiesSold * pricePerGame < 1000000):
        return cut

    copiesDownloaded -= 1000000

    if (copiesDownloaded < 100000):
        cut += copiesDownloaded * price1
        return cut
    else:
        cut += 100000 * price1
    
    copiesDownloaded -= 100000

    if (copiesDownloaded < 400000):
        cut += copiesDownloaded * price2
        return cut
    else:
        cut += 400000 * price2

    copiesDownloaded -= 400000

    if (copiesDownloaded < 500000):
        cut += copiesDownloaded * price3
        return cut
    else:
        cut += 500000 * price3
    
    copiesDownloaded -= 500000

    cut += copiesDownloaded * price4
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

# Create a figure and axes for the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)  # Adjust the bottom margin to accommodate sliders

# Define initial values for sliders
initial_devs = 3
initial_price_per_game = 5
initial_downloads_per_game = 5

# Create slider widgets
ax_devs = plt.axes([0.1, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_price_per_game = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_downloads_per_game = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')

s_devs = wplt.Slider(ax_devs, 'Devs', 1, 10, valinit=initial_devs)
s_price_per_game = wplt.Slider(ax_price_per_game, 'Price per Game', 1, 10, valinit=initial_price_per_game)
s_downloads_per_game = wplt.Slider(ax_downloads_per_game, 'Downloads per Game', 1, 10, valinit=initial_downloads_per_game)

# Function to update the plot based on slider values
def update(val):
    devs = s_devs.val
    pricePerGame = s_price_per_game.val
    downloadsPerGame = s_downloads_per_game.val
    
    # Update your calculations here based on the new slider values
    
    # Clear the previous plot and redraw it
    ax.clear()
    x = np.arange(minXValue, maxXValue, step)
    unityEarnings = np.array([(i * pricePerGame * 0.7 - calculateUnityCut(i, pricePerGame, downloadsPerGame)) / devs for i in x])
    unityPlusEarnings = np.array([(i * pricePerGame * 0.7 - calculateUnityProCut(i, pricePerGame, downloadsPerGame)) / devs - (devs * 2040) for i in x])
    epicEarnings = np.array([(i * pricePerGame * 0.7 - calculateEpicCut(i, pricePerGame)) / devs for i in x])
    godotEarnings = np.array([(i * pricePerGame * 0.7) / devs for i in x])

    minimumWage = np.array([minimumWageFunction(i) for i in x])
    averageWage = np.array([83000 for _ in x])
    
    ax.plot(x, unityEarnings, label="Unity")
    ax.plot(x, unityPlusEarnings, label="Unity Plus")
    ax.plot(x, epicEarnings, label="Epic")
    ax.plot(x, godotEarnings, label="Free engine")
    ax.plot(x, minimumWage, label="Minimum Wage", linestyle='--')
    ax.plot(x, averageWage, label="Average Dev Wage", linestyle='--')

    ax.set_xlabel("Sales")
    ax.set_ylabel("Earnings per developer")
    ax.legend()
    ax.set_title(f"Earnings per developer for different engines ({devs}: devs, {downloadsPerGame}: average downloads per buy, ${pricePerGame}USD: price per copy)")
    ax.grid(which='both')
    ax.grid(which='major', alpha=.4, linestyle='--')
    ax.grid(which='minor', alpha=.1, linestyle='--')
    ax.set_xticks(np.arange(minXValue, maxXValue, step * 10), minor=True)
    ax.set_xticks(np.arange(minXValue, maxXValue, step * 100))


    minYValues = [min(unityEarnings), min(unityPlusEarnings), min(epicEarnings), min(godotEarnings), min(minimumWage)]
    maxYValues = [max(unityEarnings), max(unityPlusEarnings), max(epicEarnings), max(godotEarnings), max(minimumWage)]

    ax.set_yticks(np.arange(min(minYValues), max(maxYValues), step * 10), minor=True)

# Attach the update function to the sliders
s_devs.on_changed(update)
s_price_per_game.on_changed(update)
s_downloads_per_game.on_changed(update)

# Initialize the plot with initial values
update(None)

plt.show()
