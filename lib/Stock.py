#This class is created to represent the different types of stocks available
#It provides the following functions:
#1. Stores the stock name, type Last Dividend, Fixed Dividend, Par Value parameters
from lib.Trade import Trade

class Stock:

    COMMON = "Common"
    PREFERRED = "Preferred"

#CLASS INITIALISATION
    def __init__(self, stockSym, stockType, lastDiv, fixedDiv, parVal):
        self.stockSym = stockSym
        self.stockType = stockType
        self.lastDiv = lastDiv
        self.fixedDiv = fixedDiv
        self.parVal = parVal

        self.timeDelta = 0

        #current market price is 0 until the stock is traded. if it's 0 it is not included
        #in the GBCE All Share Index calculations
        self.currentMarketPrice = 0
        
#PUBLIC SET FUNCTIONS
    def setCurrentMarketPrice(self, number):
        self.currentMarketPrice = float(number)

#PUBLIC CALC FUNCTIONS

    def calculateDividendYield(self):
        #calculate based on stock type by creating a dict for each different type
        #(Dividend / Market Price - for Common Stocks)
        #(Fixed Div*Par Value / Market Price - for Preferred Stocks)
        #NOTE: avoid 0 division
        if (self.currentMarketPrice != 0):
        
            return {self.COMMON: self.lastDiv/self.currentMarketPrice,
                         
                    self.PREFERRED: self.fixedDiv*self.parVal/self.currentMarketPrice
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
        
    def buyStock(self, amountIn, timeDelta = 0):
        #calls on the Trade class which will be either a buy or sell trade
        return Trade(self.stockSym, "BUY", amountIn, self.currentMarketPrice, timeDelta)
        
        
    def sellStock(self, amountIn, timeDelta = 0):
        #calls on the Trade class which will be either a buy or sell trade
        return Trade(self.stockSym, "SELL", amountIn, self.currentMarketPrice, timeDelta)

    def toString(self):
        string = "Stock Symbol: " + str(self.stockSym) + ", Stock Type: " + str(self.stockType) + ", Last Dividend: " + str(self.lastDiv) + ", Fixed Dividend: " + str(self.fixedDiv) + ", Par Val: " + str(self.parVal) + ", Current Price: " + str(self.currentMarketPrice)

        print(string) 
