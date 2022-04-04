class Room:
    def __init__(self,roomID,length, width):
        self.__rmID = roomID
        self.__rmLength = length
        self.__rmWidth = width

    def getRmID(self):
        return self.__rmID

    def setRmID(self, newID):
        self.__rmID = newID

    def getRmLength(self):
        return self.__rmLength

    def setRmLength(self, newLength):
        self.__rmLength = newLength

    def getRmWidth(self):
        return self.__rmWidth

    def setRmWidth(self, newWidth):
        self.__rmWidth = newWidth

    def calcRmArea(self):
        return self.getRmLength() * self.getRmWidth()

    def __str__(self):
        tmp = ""
        tmp += self.getRmID() + '\n'
        tmp += "Length: "+ str(self.getRmLength())+'\n'
        tmp += "Width: "+ str(self.getRmWidth()) + '\n'
        tmp += "Area: " + str(self.calcRmArea()) + '\n'
        return tmp
