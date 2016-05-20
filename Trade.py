#This class is created to store trade attributes
from datetime import datetime

class Trade:

    #CLASS INITIALISATION
    def __init__(self, stockSym, tradeType, quantity, tradePrice):
        self.stockSym = stockSym
        self.tradeType = tradeType
        self.quantity = quantity
        self.tradePrice = tradePrice
        self.timestamp = datetime.now()

    #TO STRING METHOD (for testing)
    def toString(self):
        string = "Stock Symbol: " + str(self.stockSym) + ", Trade Type: " + str(self.tradeType) + ", Quantity: " + str(self.quantity) + ", Trade Price: " + str(self.tradePrice) + ", Timestamp: " + str(self.timestamp)
        print(string) 
    
