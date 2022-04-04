class Vehicle:
    __nextID = 1000

    def __init__(self, make, MSRP, sellPrice):
        self.__make = make
        self.__MSRP = MSRP
        self.__sellPrice = sellPrice
        self.__id = Vehicle.__nextID
        Vehicle.__nextID += 100

    def getID(self):
        return self.__id

    def getMake(self):
        return self.__make
    
    def getMSRP(self):
        return self.__MSRP

    def getSellPrice(self):
        return self.__sellPrice
    
    def calcProfit(self):
        return (self.getSellPrice() - self.getMSRP())

    
    def __str__(self):
        return "ID: " + str(self.getID()) +\
            "\nMake: " + str(self.getMake()) +\
                "\nMSRP: " + str(self.getMSRP()) +\
                    "\nSell Price: " + str(self.getSellPrice())