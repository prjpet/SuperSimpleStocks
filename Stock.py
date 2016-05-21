#This class is created to represent the different types of stocks available
#It provides the following functions:
#1. Stores the stock name, type Last Dividend, Fixed Dividend, Par Value parameters
from Trade import Trade

class Stock:

#CLASS INITIALISATION
    def __init__(self, stockSym, stockType, lastDiv, fixedDiv, parVal):
        self.stockSym = stockSym
        self.stockType = stockType
        self.lastDiv = lastDiv
        self.fixedDiv = fixedDiv
        self.parVal = parVal
        
#PUBLIC SET FUNCTIONS
    def setCurrentMarketPrice(self, number):
        self.currentMarketPrice = number

#PUBLIC CALC FUNCTIONS

    def calculateDividendYield(self):
        #calculate based on stock type by creating a dict for each different type
        #(Dividend / Market Price - for Common Stocks)
        #(Fixed Div*Par Value / Market Price - for Preferred Stocks)
        #NOTE: avoid 0 division
        if (self.currentMarketPrice != 0):
        
            return {"Common": self.lastDiv/self.currentMarketPrice,
                         
                    "Preferred": self.fixedDiv*self.parVal/self.currentMarketPrice
                    #then return the value from the dict based on actual stock type
                    }[self.stockType]
        
        else:
            return 0

    def calculatePERatio(self):
        #return the value of the equation (Market Price / Dividend)
        #NOTE: avoid 0 division
        if (self.lastDiv != 0):
            return self.currentMarketPrice / self.lastDiv
        else:
            return 0
                        
#PUBLIC TRADING CALLS
#these set of functions will return an instance of the trade class passing relevant data to the class
#args: Stock Symbol, Trade type, traded amount, calculated trade price - at the moment the Trade class is instantiated it is timestamped within the Init block
        
    def buyStock(self, amountIn):
        #calls on the Trade class which will be either a buy or sell trade
        return Trade(self.stockSym, "BUY", amountIn, self.currentMarketPrice)
        
        
    def sellStock(self, amountIn):
        #calls on the Trade class which will be either a buy or sell trade
        return Trade(self.stockSym, "SELL", amountIn, self.currentMarketPrice)
        
