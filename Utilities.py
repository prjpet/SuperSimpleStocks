#THe utilities class has been made to incorporate all of the verification methods
#If the utilities class is doing any verification on existing data structures
#then the data structure will be passed as an argument to the class upon initialisation
from TradesManager import TradesManager


class Utilities:
    ISVALIDPRICE = "isvalidprice"
    BUYORSELL = "buyorsell"
    AMOUNT = "amount"
    STOCKNAME = "stockname"

    def __init__(self, StockManager):
        self.myStockManager = StockManager
        self.verificationMap = {self.ISVALIDPRICE: self.isValidPrice,
                                self.BUYORSELL: self.verifyBuyOrSell,
                                self.AMOUNT: self.verifyAmount,
                                self.STOCKNAME: self.verifyStockName
                                }

    #PUBLIC DISPLAY METHODS
    def displayWelcome(self, dictOfStocks):
      for stock in dictOfStocks:
        dictOfStocks[stock].toString()
      print("---------------------------------------------------------------")
        
    def displayUserPrompt(self, promptText, failureText, verificationMethod):
        print(promptText)
        userInput = input("-->")
        userInput = self.verifyUserInput(userInput, verificationMethod, failureText)

        return userInput

    #This method below uses one of the other methods to verify the validity of user input
    #the verification method is selected using the mapping of class constants to the method

    def verifyUserInput(self, receivedText, verificationMethod, textToDisplay):

        #As this is utilities for the programmer, validation is not required, as any error
        #should be treated by programmer (i.e.: constants should be used)
        while (not self.verificationMap[verificationMethod](receivedText)):
            print(textToDisplay)
            receivedText = input("-->")
        return receivedText

    #PRIVATE VERIFICATION FUNCTIONS MAPPED TO CONSTANTS in __init__

    def isValidPrice(self, value):
    #price has to be >0 and float value
    #0 price is for stocks which have not been traded before
      result = False
      try:
        float(value)
        result = True
      except:
        result = False

      if (not((result == True) and (float(value) > 0))):
          result = False
          
      return result

    def verifyBuyOrSell(self, string):
      if (string.upper() == TradesManager.BUY) or (string.upper() == TradesManager.SELL):
        return True
      else:
        return False

    def verifyAmount(self, value):
      #amount has to be bigger than 0 and int value
      #0 price is for stocks which have not been traded before
      result = False
      try:
        int(value)
        result = True
      except:
        result = False

      if (not((result == True) and (int(value) > 0))):
          result = False
          
      return result

    def verifyStockName(self, string):
      if string.upper() in self.myStockManager.listOfStocks:
          return True
      else:
          return False
