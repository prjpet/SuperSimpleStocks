from Stock import Stock

class StockManager:

    def __init__(self):
        self.listOfStocks = {"TEA": Stock("TEA", "Common", 0, 0, 100),
                             "POP": Stock("POP", "Common", 8, 0, 100),
                             "ALE": Stock("ALE", "Common", 23, 0, 60),
                             "GIN": Stock("GIN", "Preferred", 8, 0.02, 100),
                             "JOE": Stock("JOE", "Common", 13, 0, 200)
                             }
        
