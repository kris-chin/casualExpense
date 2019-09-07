'''

    Author: Krischin Layon

    Graphs the money bleeding from your wallet.
    Each recurring expense is represented as an expense object that contains a name, initial cost, and recurrance rate

    #TODO: add easy identification of amounts after certain days
    #TODO: add a way to adjust the paramaters of each expense to see how to fix your budget

    main.py


'''

from matplotlib import pyplot as plt
from matplotlib import ticker as tick
import numpy as np
import random

from Expense import *

def main():
    expenses = [
        Expense("Coffee",2.45,1),
        Expense("Gas", 20, 4),
        Expense("Lunch",6.59,1,spread=(0,4))
    ]

    #start pyplot
    fig = plt.figure()
    ax = plt.axes()

    days = np.linspace(0,14,15)
    totalCost = 0
    totalCostPlot = [] #y's of the total cost at a particular point in time

    for d in days:
        for e in expenses: #go through every expense we listed
            if d%e.rate == 0: #if its time to add another purchase
                if e.spread != (0,0):
                    randValue = random.uniform(-e.spread[0],e.spread[1]) #calculate the variance in the purchase
                else:
                    randValue = 0
                totalCost += (e.cost + randValue)
                e.cumCost += (e.cost + randValue)
                e.count+=1
            e.plot.append(e.cumCost)

        totalCostPlot.append(totalCost)
    
    plt.plot(days,totalCostPlot,label = "Total Expenses",color = "black")

    #plot expenses
    for e in expenses: plt.plot(days,e.plot,label=(e.name + ": $" + str(e.cost) + " ±\$(" + str(e.spread[0]) + ", " + str(e.spread[1]) + ") every ~" + str(e.rate) +" days") )

    #ticks
    plt.xticks(days)
    ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x:,.0f}')) #add the dollar signs to the y axis
    ax.legend()
    #labels
    plt.title("The cost of your actions")
    plt.xlabel("Days")
    plt.ylabel("Cash Outflow (USD)")
    plt.show()


main()