from Trade import Trade
from StockManager import StockManager
from datetime import datetime

class TradesManager:
    #CLASS INITIALISATION
    def __init__(self):
        self.tradeRecord = {}
        self.vwapLastFifteen = {}
        

    #PUBLIC POPULATE FUNCTIONS
    def appendNewTrade(self, tradeToAppend):

        #if the stock has already been traded 
        if tradeToAppend.stockSym in self.tradeRecord:
            #the consecutive trades can be appended to the list which is attached to the stockSym
            self.tradeRecord[tradeToAppend.stockSym].append(tradeToAppend)
        else:
            #the very first trade needs to be wrapped into a list
            self.tradeRecord[tradeToAppend.stockSym] = [tradeToAppend]

        #each and every trade should generate the recalculation of the VWSP
        calcVWAP(15, stockSym)

    #PRIVATE CALC FUNCTIONS
    def calcCWAP(self, period, stockSym):
        
        timeLimit = datetime.now()-datetime.timedelta(minutes=period)
        print(timeLimit)

        #iterate through all available trades for the specific stockSym
        for tradeList in self.tradeRecord[stockSym]:
            for trade in tradeList:
                #if timestamp is less than time limit (i.e.: less than 15 minutes before now)
                if (trade.timestamp < timeLimit):
                    

                

    #TO STRING (for testing)
    def allTradesToString(self):
        for stock in self.tradeRecord:
            for item in self.tradeRecord[stock]:
                item.toString()
    
