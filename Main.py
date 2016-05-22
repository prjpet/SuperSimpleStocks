import sys

from Stock import Stock
from TradesManager import TradesManager
from StockManager import StockManager
from Utilities import Utilities

#PROGRAM FLOW:
prompt1 = "Please choose one of the available stocks (from above) for trading: "
prompt2 = "Only the displayed stock symbols are accepted. Try again."

prompt3 = "Please input current market price for stock "
prompt4 = "Only numerical (float - dot separated) input is accepted. Try again."

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
    floatIn = myUtilities.displayUserPrompt(prompt3 + currentStock, prompt4, myUtilities.ISFLOAT)
    
    #Step 3.: store the given price in Stock Class
    myStockManager.listOfStocks[currentStock].setCurrentMarketPrice(float(floatIn))

    #Step 4.: Calculate and display Dividend Yield
    print("The dividend yield of stock based on stock price and stock type is:")
    print(myStockManager.listOfStocks[currentStock].calculateDividendYield())

    #Step 5.: Calculate and display P/E Ratio
    print("The P/E ratio of stock based on stock price and last dividend is:")
    print(myStockManager.listOfStocks[currentStock].calculatePERatio())

    #Step 6.: Record a Trade. Buy or Sell?
    tradeTypeIn = myUtilities.displayUserPrompt(prompt5, prompt6, myUtilities.BUYORSELL)

    #Step 7.: Amount?
    amountToDeal = myUtilities.displayUserPrompt(prompt7, prompt8, myUtilities.AMOUNT)
    
    #Step 7.: Register Trade
    if (tradeTypeIn.upper() == "BUY"):

      myTradesManager.appendNewTrade(myStockManager.listOfStocks[currentStock].buyStock(int(amountToDeal)))
      myTradesManager.updateVWAPLastFifteen(currentStock)
      myTradesManager.displayAllData()
      
    elif(tradeTypeIn.upper() == "SELL"):

      myTradesManager.appendNewTrade(myStockManager.listOfStocks[currentStock].sellStock(int(amountToDeal)))
      myTradesManager.updateVWAPLastFifteen(currentStock)
      myTradesManager.displayAllData()
