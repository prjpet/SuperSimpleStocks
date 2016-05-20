from Trade import Trade
from datetime import datetime

class TradesManager:
    #CLASS INITIALISATION
    def __init__(self):
        self.tradeRecord = []

    #PUBLIC POPULATE FUNCTIONS
    def appendNewTrade(self, tradeToAppend):
        self.tradeRecord.append(tradeToAppend)

    #PUBLIC CALC FUNCTIONS
    def volumeWeightedStockPrice(self):

        if (len(self.tradeRecord) > 0):
            timeLimit = datetime.now()-datetime.timedelta(minutes=15)
            print(timeLimit)

            #iterate through all available trades
            for trade in self.tradeRecord:
                #if timestamp is less than time limit (i.e.: less than 15 minutes before now)
                if (trade.timestamp < timeLimit):
                    print("Dummy")

            
        #else:
            #the value would be 0 anyway if there aren't any trades
            

    #TO STRING (for testing)
    def allTradesToString(self):
        for item in self.tradeRecord:
            item.toString()
    
