import sys

class FileReader:

    READ = "read"

    def __init__(self, filename, accessRight):
        #create class attributes NOTE: accessRight not in use ATM only for future
        self.file = None
        self.trades = []

        self.openFile(filename, accessRight)
        self.readAllTradesIn()

    #create skeleton to enable further expansion opportunities
    def openFile(self, filename, accessRight):
        try:
            self.file = open(filename, "r")
        except:
            print("An error occured while trying to open the file")

    def readAllTradesIn(self):
        for line in self.file:

            lineList = line.split(",")

            #ignore lines starting with a hashtag
            if (lineList[0][0] != "#"):
                self.trades.append([lineList[0], lineList[1], lineList[2], lineList[3], lineList[4][:-1]])

    def allTradesToString(self):
        for trade in self.trades:
            print(trade)

#for testing
#if __name__ == '__main__':
    #myFileReader = FileReader()
    #myFileReader.allTradesToString()
