from lib.Stock import Stock
from lib.TradesManager import TradesManager
from lib.StockManager import StockManager
from lib.Utilities import Utilities


#PROGRAM FLOW:
prompt1 = "Please choose one of the available stocks (from above) for trading: "
prompt2 = "Only the displayed stock symbols are accepted. Try again."

prompt3 = "Please input current market price for stock "
prompt4 = "Only numerical (float - dot separated) input is accepted, which is bigger than 0. Try again."

prompt5 = "Register Trade: Buy or Sell?"
prompt6 = "Only the words buy or sell are accepted. Try again."

prompt7 = "Please enter amount traded as a whole number: "
prompt8 = "Only whole numbers are accepted. Try again."

if __name__ == '__main__':

  #Step 0.: Build list of stocks by StockManager, create Trade Manager and Utitlities
  myStockManager = StockManager()
  myTradesManager = TradesManager(myStockManager)
  myUtilities = Utilities(myStockManager)

  #Trigger new trade cycle for manual input of trades
  while(True):
    myUtilities.displayWelcome(myStockManager.listOfStocks)
    
    #Step 1.: Display all available stocks and prompt user to choose one:
    currentStock = myUtilities.displayUserPrompt(prompt1, prompt2, myUtilities.STOCKNAME).upper()
    
    #..and ask for the current market price for it:
    floatIn = myUtilities.displayUserPrompt(prompt3 + currentStock, prompt4, myUtilities.ISVALIDPRICE)
    
    #Step 3.: store the given price in Stock Class
    myStockManager.listOfStocks[currentStock].setCurrentMarketPrice(float(floatIn))

    #Step 4.: Calculate and display Dividend Yield
    print("---------------------------------------------------------------")
    print("The dividend yield of stock based on stock price and stock type is: ", myStockManager.listOfStocks[currentStock].calculateDividendYield())
    print("---------------------------------------------------------------")
    #Step 5.: Calculate and display P/E Ratio
    print("The P/E ratio of stock based on stock price and last dividend is: ", myStockManager.listOfStocks[currentStock].calculatePERatio())
    print("---------------------------------------------------------------")

    #Step 6.: Record a Trade. Buy or Sell?
    tradeTypeIn = myUtilities.displayUserPrompt(prompt5, prompt6, myUtilities.BUYORSELL).upper()

    #Step 7.: Amount?
    amountToDeal = int(myUtilities.displayUserPrompt(prompt7, prompt8, myUtilities.AMOUNT))
    
    #Step 7.: Register Trade
    if (tradeTypeIn == myTradesManager.BUY):

      myTradesManager.appendNewTrade(myStockManager.listOfStocks[currentStock].buyStock(amountToDeal))
      myTradesManager.displayAllData()
      
    elif(tradeTypeIn == myTradesManager.SELL):

      myTradesManager.appendNewTrade(myStockManager.listOfStocks[currentStock].sellStock(amountToDeal))
      myTradesManager.displayAllData()
