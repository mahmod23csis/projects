from datetime import *

class Person:
    __nextID = 100
    __population = 0

    def __init__(self, tmpName):
        self.__name = tmpName
        self.__id = Person.__nextID
        Person.__nextID += 10
        Person.__population += 1

    def getName(self):
        return self.__name

    def getID(self):
        return self.__id

    def getPopulation():
        return Person.__population
        
    def setName(self, newName):
        self.__name = newName
        
    def __str__(self):
        return "ID: " + str(self.getID()) + \
            " Name: " + self.getName()

class Student(Person):
    __numBioMajors = 0

    def __init__(self, tName, tMajor):
        self.__major = tMajor
        if tMajor == "Biology":
            Student.__numBioMajors += 1
        Person.__init__(self, tName)

    def getMajor(self):
        return self.__major
    
    def getNumBioMajors():
        return Student.__numBioMajors
    
    def __str__(self):
        tmp = Person.__str__(self)
        tmp += " Major: " + self.getMajor()
        return tmp