from Trade import Trade
from StockManager import StockManager
import datetime

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
            

    def updateVWAPLastFifteen(self, stockSym):
        #for simplicity each and every trade will generate the recalculation of the VWAP
        self.vwapLastFifteen[stockSym] = self.calculateVWAP(15, stockSym)

    #PRIVATE CALC FUNCTIONS
    def calculateVWAP(self, period, stockSym):

        sumOfTradePriceQuantity = 0
        sumOfVolume = 0

        #set the time limit to be the the period before now
        timeLimit = datetime.datetime.now()-datetime.timedelta(minutes=period)

        #iterate through all available trades for the specific stockSym
        for trade in self.tradeRecord[stockSym]:
            #if timestamp is more than time limit (i.e.: less than 15 minutes before now)
            if (trade.timestamp > timeLimit):
                
                sumOfTradePriceQuantity += float(trade.quantity)*trade.price
                sumOfVolume += trade.quantity

        return sumOfTradePriceQuantity/sumOfVolume

    #TO STRING (for testing)
    def allTradesToString(self):
        for stock in self.tradeRecord:
            for item in self.tradeRecord[stock]:
                item.toString()
            print("The VWAP of trades from the last 15 mins is: ", self.vwapLastFifteen[stock])
    
