from lib.Stock import Stock

class StockManager:

    def __init__(self):
        self.listOfStocks = {"TEA": Stock("TEA", Stock.COMMON, 0, 0, 100),
                             "POP": Stock("POP", Stock.COMMON, 8, 0, 100),
                             "ALE": Stock("ALE", Stock.COMMON, 23, 0, 60),
                             "GIN": Stock("GIN", Stock.PREFERRED, 8, 0.02, 100),
                             "JOE": Stock("JOE", Stock.COMMON, 13, 0, 200)
                             }
        
