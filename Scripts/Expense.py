'''

    Expense.py

    Holds the Expense class which holds:
        -a single cost value (float): the price of the expense
        -reccurrance rate (int): number of days before another purchase is made. ex. 1 = daily, 7 = weekly, etc.

'''

class Expense():
    def __init__(self,name,cost,rate=1,spread=(0,0)):
        self.name = name #name of the expense
        self.cost = cost #exact price of the expense
        self.rate = rate #how many days before you make the expense again
        self.spread = spread #how much to vary each purchase every time its made. first element is lowest, second element is highest (simulates buying different lunches in roughly the same range) defaults to 0

        #plot stuff
        self.count = 0 #the number of times the purchase has been made
        self.cumCost = 0
        self.plot = [] #plot of the value over time