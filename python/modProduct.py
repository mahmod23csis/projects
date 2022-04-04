__author__="Mahmod Ahmad"
__date__="10/28/2020"

"""In this main file we created our Product class which consists
of our constructor, getters, setters, and our string converter."""

from datetime import *
class Product:
    def __init__(self, productID, name, quantity, price, productDate):
        self.__prodID = productID
        self.__prodName = name
        self.__ProdQuantity = quantity
        self.__prodPrice = price
        self.__prodDate = productDate
    
    def getProdID(self):
        return self.__prodID
    
    def setProdID(self, newID):
        self.__prodID = newID

    def getProdName(self):
        return self.__prodName
    
    def setProdName(self, newName):
        self.__prodName = newName

    def getProdQuantity(self):
        return self.__ProdQuantity
    
    def setProdQuantity(self, newQuantity):
        self.__ProdQuantity = newQuantity
    
    def getProdPrice(self):
        return self.__prodPrice

    def setProdPrice(self, newPrice):
        self.__prodPrice = newPrice

    def getProdDate(self):
        return self.__prodDate
    
    def setProdDate(self, newProdDate):
        self.__prodDate = newProdDate
        
    def ProductionDate(self):
        dateObj = datetime.strftime(self.getProdDate(), "%m-%d-%Y")
        return dateObj
        
    def ProdAge(self):
        curDate = datetime.today()
        prodDate = self.getProdDate()
        return (curDate.year - prodDate.year - ((curDate.month, curDate.day) < \
                                                   (prodDate.month, prodDate.day)))
    
    def __str__(self):
        id = self.getProdID(); name = self.getProdName()
        quantity = self.getProdQuantity(); price = self.getProdPrice()
        production = self.ProductionDate(); age = str(self.ProdAge())
        tmp = "ID: {:5s}\nName: {:10s}\nQuantity: {:5}\nPrice: ${:5.2f}\
        \nProduction Date: {:12s}\nProduct Age: {:3}years".format(id, name,\
        quantity, price, production, age)
        return tmp
