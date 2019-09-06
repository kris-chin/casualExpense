'''

    Author: Krischin Layon

    Graphs the money bleeding from your wallet.

    Each recurring expense is represented as an expense object that contains a name, initial cost, and recurrance rate

    main.py


'''

from matplotlib import pyplot as plt
import numpy as np

from Expense import *

def main():
    expenses = [
        Expense("Coffee ($2.45)",2.45,1),
        Expense("Gas ($20)", 20, 3),
        Expense("Mom Money (-$100)", -100, 7)
    ]

    #start pyplot
    fig = plt.figure()
    ax = plt.axes()

    days = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    totalCost = 0
    totalCostPlot = []

    for d in days:
        for e in expenses: #go through every expense we listed
            if d%e.rate == 0: #if its time to add another purchase
                totalCost += (e.count*e.cost)
                e.count+= 1
        totalCostPlot.append(totalCost)
    
    plt.plot(days,totalCostPlot,label = "Total Expenses")

    #ticks
    plt.xticks(days)
    ax.legend()
    #labels
    plt.title("The cost of your actions")
    plt.xlabel("Days")
    plt.ylabel("Cash Outflow (USD)")
    plt.show()


main()