class Student:
    __nextID = 100
    __numStudents = 0

    def __init__(self, tmpName, tmpMajor, tmpGPA):  #ID NOT PASSED IN
        self.__ID = Student.__nextID
        Student.__nextID += 10
        Student.__numStudents += 1
        self.__name = tmpName
        self.__major = tmpMajor
        self.__GPA = tmpGPA

    def getID(self):
        return self.__ID    #NO SETTER FOR THE ID

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def getMajor(self):
        return self.__major

    def setMajor(self, newMajor):
        self.__major = newMajor

    def getGPA(self):
        return self.__GPA

    def setGPA(self, newGPA):
        self.__GPA = newGPA

    def __str__(self):
        tmp = str(self.getID()) + "\n" + self.getName() + "\n" + \
              self.getMajor() + "\n" + str(self.getGPA()) + "\n"
        return tmp

    def getNumStudents():
        return Student.__numStudents
