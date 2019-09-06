'''

    Expense.py

    Holds the Expense class which holds:
        -a single cost value (float): the price of the expense
        -reccurrance rate (int): number of days before another purchase is made. ex. 1 = daily, 7 = weekly, etc.

'''

class Expense():
    def __init__(self,name,cost,rate=1):
        self.name = name
        self.cost = cost
        self.rate = rate
        
        self.count = 0 #the number of times the purchase is made