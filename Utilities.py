#THe utilities class has been made to incorporate all of the verification methods
#If the utilities class is doing any verification on existing data structures
#then the data structure will be passed as an argument to the class upon initialisation

class Utilities:

    def __init__(self, StockManager):
        self.myStockManager = StockManager
        self.verificationMap = {"isfloat": self.isfloat,
                                "buyorsell": self.verifyBuyOrSell,
                                "amount": self.verifyAmount,
                                "stockname": self.verifyStockName
                                }

    #PUBLIC METHOD
    def verifyUserInput(self, receivedText, verificationMethod, textToDisplay):
        #As this is utilities for the programmer, validation is not required, as any error
        #should be treated by programmer (i.e.: constants should be used)

        while (not self.verificationMap[verificationMethod](receivedText)):
            print(textToDisplay)
            receivedText = input("-->")
        return receivedText

    #PRIVATE VERIFICATION FUNCTIONS
    def isfloat(self, value):
      print("isfloat called with value: ", value)
      try:
        float(value)
        return True
      except:
        return False

    def verifyBuyOrSell(self, string):
      if (string.upper() == "BUY") or (string.upper() == "SELL"):
        return True
      else:
        return False

    def verifyAmount(self, value):
      try:
        int(value)
        return True
      except:
        return False

    def displayAllStocks(self, dictOfStocks):
      for stock in dictOfStocks:
        print(stock)

    def verifyStockName(self, string):
      if string.upper() in self.myStockManager.listOfStocks:
          return True
      else:
          return False
