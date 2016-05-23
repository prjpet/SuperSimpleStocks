import datetime
import functools

class TradesManager:
    BUY = "BUY"
    SELL = "SELL"
    
    #CLASS INITIALISATION
    def __init__(self, myStockManager):
        self.tradeRecord = {}
        self.myStockManager = myStockManager

    #PUBLIC POPULATE FUNCTIONS
    def appendNewTrade(self, tradeToAppend):

        #if the stock has already been traded 
        if tradeToAppend.stockSym in self.tradeRecord:
            #the consecutive trades can be appended to the list which is attached to the stockSym
            self.tradeRecord[tradeToAppend.stockSym].append(tradeToAppend)
        else:
            #the very first trade needs to be wrapped into a list
            self.tradeRecord[tradeToAppend.stockSym] = [tradeToAppend]

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
                
                sumOfTradePriceQuantity += trade.quantity*trade.price
                sumOfVolume += trade.quantity

        return sumOfTradePriceQuantity/sumOfVolume

    def calculateGBCEAllShareIndex(self):
        listOfPrices = []
        #depending on whether the stock has been traded already, include it in the calculation
        #we have already made sure that all the values will be more than 0 if once traded
        for stock in self.myStockManager.listOfStocks:
            if (self.myStockManager.listOfStocks[stock].currentMarketPrice != 0):
               listOfPrices.append(self.myStockManager.listOfStocks[stock].currentMarketPrice)

        #using the reduce function for better efficiency collate the numbers included in the list together
        #and using formula (1*2*...n)**(1/n) return geometric mean
        #for better accuracy, external open source libraries could be used
               
        return (functools.reduce(lambda x, y: x*y, listOfPrices))**(1.0/len(listOfPrices))

    #TO STRING
    def displayAllData(self):
        for stock in self.tradeRecord:
            print("---------------------------------------------------------------")
            print("Trades for " + stock + " stock:")
            print("---------------------------------------------------------------")
            #for each trade / stock display the trade details
            for item in self.tradeRecord[stock]:
                item.toString()
            #after displaying all trades display the current VWAP
            print("---------------------------------------------------------------")
            print("The VWAP of trades for " + stock + " from the last 15 mins is: ", self.calculateVWAP(15, stock))
            print("---------------------------------------------------------------")
        #and last, display GBCE All Share Index
        print("----------------------------------------------------------")          
        print("The GBCE All Share Index for all the shares is: ", self.calculateGBCEAllShareIndex())
        print("----------------------------------------------------------") 
