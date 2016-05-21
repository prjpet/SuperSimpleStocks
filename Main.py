import sys
from Stock import Stock
from TradesManager import TradesManager
from StockManager import StockManager


def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

def verifyBuyOrSell(string):
  if (string.upper() == "BUY") or (string.upper() == "SELL"):
    return True
  else:
    return False

def verifyAmount(value):
  try:
    int(value)
    return True
  except:
    return False

def displayAllStocks(dictOfStocks):
  for stock in dictOfStocks:
    print(stock)

def verifyStockName(string, dictOfStocks):
  if string in dictOfStocks:
      return True
  else:
      return False

#Referring to __main__ in order to make Main class re-usable in future
if __name__ == '__main__':
  #Step 0.: Initialise TradesManager and StockManager
  myTradesManager = TradesManager()
  myStockManager = StockManager()
  
  while(True):
    
    #Step 1.: Display all available stocks and prompt user to choose one:
    print("Please choose one of the following stocks for trading (or type ex to terminate): ")
    displayAllStocks(myStockManager.listOfStocks)

    stockToTradeIn = input("-->")
    while (not verifyStockName(stockToTradeIn.upper(), myStockManager.listOfStocks)) and (not (stockToTradeIn.upper() == "ex".upper())):
        print("Only the displayed stock symbols or ""ex"" are accepted. Try again.")
        stockToTradeIn = input("-->")

    #Terminate application on ex
    if (stockToTradeIn.upper() == "ex".upper()):
      sys.exit()

    
    #Step 2.: To be able to keep currentStock variable from 1. Commit:
    currentStock = stockToTradeIn.upper()
    #..and ask for the current market price...
    print("Please input current market price for " + currentStock + " stock:")

    #...until a number is given in float format.
    floatIn = input("-->")
    while (not isfloat(floatIn)):
        print("Only numerical (float - dot separated) input is accepted. Try again.")
        floatIn = input("-->")

    #Step 3.: store the given price in Stock Class
    myStockManager.listOfStocks[currentStock].setCurrentMarketPrice(float(floatIn))

    #Step 4.: Calculate and display Dividend Yield
    print("The dividend yield of stock based on stock price and stock type is:")
    print(myStockManager.listOfStocks[currentStock].calculateDividendYield())

    #Step 5.: Calculate and display P/E Ratio
    print("The P/E ratio of stock based on stock price and last dividend is:")
    print(myStockManager.listOfStocks[currentStock].calculatePERatio())

    #Step 6.: Record a Trade. Buy or Sell?
    print("Buy or Sell? (Please type either buy / sell below):")
    #...until the input is the correct word.
    tradeTypeIn = input("-->")
    while (not verifyBuyOrSell(tradeTypeIn)):
        print("Only the words buy or sell are accepted. Try again.")
        tradeTypeIn = input("-->")

    #Step 7.: Amount?
    print("Please enter amount to buy or sell as a whole number: ")
    #...until the input is valid amount.
    amountToDeal = input("-->")
    while (not verifyAmount(amountToDeal)):
        print("Only whole numbers are accepted. Try again.")
        amountToDeal = input("-->")

        
    #Step 7.: Register Trade
    if (tradeTypeIn.upper() == "BUY"):

      myTradesManager.appendNewTrade(myStockManager.listOfStocks[currentStock].buyStock(int(amountToDeal)))
      myTradesManager.updateVWAPLastFifteen(currentStock)
      myTradesManager.allTradesToString()
      

    elif(tradeTypeIn.upper() == "SELL"):

      myTradesManager.appendNewTrade(myStockManager.listOfStocks[currentStock].sellStock(int(amountToDeal)))
      myTradesManager.updateVWAPLastFifteen(currentStock)
      myTradesManager.allTradesToString()

        
