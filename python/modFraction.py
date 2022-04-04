class MyFraction:
    def __init__(self, tNum=0, tDen=1):
        self.__numer = tNum
        if tDen == 0:
            self.__denom = 1
        else:
            self.__denom = tDen

    def __str__(self):
        return str(self.__numer) + "/" +\
               str(self.__denom) + "\n"

    def __mul__(f1, f2):
        resNum = f1.__numer * f2.__numer
        resDenom = f1.__denom * f2.__denom
        resFraction = MyFraction(resNum, resDenom)
        return(resFraction)
