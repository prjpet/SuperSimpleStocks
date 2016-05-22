#THe utilities class has been made to incorporate all of the verification methods
#If the utilities class is doing any verification on existing data structures
#then the data structure will be passed as an argument to the class upon initialisation

class Utilities:
    ISFLOAT = "isfloat"
    BUYORSELL = "buyorsell"
    AMOUNT = "amount"
    STOCKNAME = "stockname"

    def __init__(self, StockManager):
        self.myStockManager = StockManager
        self.verificationMap = {self.ISFLOAT: self.isfloat,
                                self.BUYORSELL: self.verifyBuyOrSell,
                                self.AMOUNT: self.verifyAmount,
                                self.STOCKNAME: self.verifyStockName
                                }

    #PUBLIC DISPLAY METHODS
    def displayWelcome(self, dictOfStocks):
      for stock in dictOfStocks:
        print(stock)
        
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
    def isfloat(self, value):
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

    def verifyStockName(self, string):
      if string.upper() in self.myStockManager.listOfStocks:
          return True
      else:
          return False
