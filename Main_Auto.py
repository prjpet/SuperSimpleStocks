from lib.Stock import Stock
from lib.TradesManager import TradesManager
from lib.StockManager import StockManager
from lib.Utilities import Utilities
from lib.FileReader import FileReader

if __name__ == '__main__':
  #in auto mode use the new file reader class to read all submitted trades from the given .csv file
  myFileReader = FileReader("TradeSource.csv", FileReader.READ)

  #Step 0.: Build list of stocks by StockManager, create Trade Manager and Utitlities
  myStockManager = StockManager()
  myTradesManager = TradesManager(myStockManager)
  myUtilities = Utilities(myStockManager)

  lineCount = 1 #starts from 1 as the first line in the file of current format is the headers

  #Read all items from within the FileReader's trades list
  for trade in myFileReader.trades:

    #Based on current formatting lineCount is correct, but not dynamically adjusting
    lineCount += 1

    #Step 1.: The first item is the stock name
    if (myUtilities.verifyStockName(trade[0])):
      currentStock = trade[0]
    else:
      currentStock = "BAD_NAME"
    
    #,second item current price
    if (myUtilities.isValidPrice(trade[1])):
      floatIn = float(trade[1])
    else:
      floatIn = 1.0
    
    #Step 3.: store the given price for given stock in Stock Class
    myStockManager.listOfStocks[currentStock].setCurrentMarketPrice(floatIn)

    #Step 4.: Record a Trade. Buy or Sell?
    if (myUtilities.verifyBuyOrSell(trade[2])):
      tradeTypeIn = trade[2]
    else:
      tradeTypeIn = "BAD_NAME"

    #Step 5.: Amount?
    if (myUtilities.verifyAmount(trade[3])):
      amountToDeal = int(trade[3])
    else:
      amountToDeal = 1

    #Is the timedelta given in an integer format?
    try:
      trade[4] = int(trade[4])
    #if not - make it 0
    except:
      trade[4] = 0

    #if the trade timestamp is bigger than 14
    if (trade[4] > 14):
      try:
        #but evidently no trades have been recorded for the stock yet
        len(myTradesManager.tradeRecord[currentStock])
      except:
        #modify timestamp adjustment to 0 to allow calculations to happen
        trade[4] = 0

    #Step 6.: Calculate and display Dividend Yield
    #Step 7.: Calculate and display P/E Ratio
    print("Registering trade from line no. ", lineCount ,": ", currentStock, ", ", floatIn, ", ", tradeTypeIn, ", ", amountToDeal, ", ", trade[4])
    print("---------------------------------------------------------------")
    print("The dividend yield of stock based on stock price and stock type is: ", myStockManager.listOfStocks[currentStock].calculateDividendYield())
    print("---------------------------------------------------------------")
    print("The P/E ratio of stock based on stock price and last dividend is: ", myStockManager.listOfStocks[currentStock].calculatePERatio())
    print("---------------------------------------------------------------")
    
    #Step 8.: Register Trade
    if (tradeTypeIn == myTradesManager.BUY):
      
      myTradesManager.appendNewTrade(myStockManager.listOfStocks[currentStock].buyStock(amountToDeal, trade[4]))
      
    elif(tradeTypeIn == myTradesManager.SELL):

      myTradesManager.appendNewTrade(myStockManager.listOfStocks[currentStock].sellStock(amountToDeal,  trade[4]))

  #Only display data at the end of all trades
  myTradesManager.displayAllData()
