__author__="Mahmod Ahmad"

"""This program asks the user to choose a file to read that has
inventory data in it. Then, the user can add a new product,
sort existing products by quantity from low to high, or
print the inventory"""

"""
Text file should look like this example:
ID, itemName, price, quantity
111, chair, 54.25, 10
112, couch, 290, 5
"""

import os.path
def createMenu(listOfChoices, menuTitle):
    menuStr=menuTitle
    for n in range(len(listOfChoices)):
        menuStr+="\n"+str(n+1)+". "+listOfChoices[n]
    return menuStr

def getValidChoice(numOptions, menuStr):
        print(menuStr)
        choice = input("Enter your choice: ")
        while choice.isdigit()==False or int(choice) > numOptions \
              or int(choice) < 1:
            print("Invalid choice. Please try again!")
            print(menuStr)
            choice = input("Enter your choice: ")
        return int(choice)
    
def openFile(prodDict, fName):
    fObj = open(fName,"r")
    line_list = fObj.readlines()
    for line in line_list:
        line = line.strip("\n")
        myList = line.split(", ")
        valList = myList[1:]
        prodDict[myList[0]] = valList
    fObj.close()

def addProduct(prodDict):
    id_in = int(input("Enter ID: "))
    des_in = input("Enter Description: ")
    price_in = input("Enter Unit Price: ")
    quantity_in = input("Enter Quantity: ")
    prodDict[id_in]=[des_in, price_in, quantity_in]
    
def sortByQuantity(prodDict):
    sortedDict = []
    for k, valList in prodDict.items():
        sort_D = valList[2]
        sortedDict.append(int(sort_D))
        sortedDict.sort()
    newDict = { }
    for sort_D in sortedDict:
        for k, valList in prodDict.items():
            if (int(valList[2])) == sort_D:
                newDict[k] = valList
    printReport(newDict)

def printReport(prodDict):
    grandTotal = 0
    print("\n", 30*" ", "Product Roster")
    print(" ")
    print("{0:5}\t{1:10}\t\t{2:10}\t{3:10}\t   {4:10}".format("ID", "Description", \
                        "Unit Price", "Quantity", "TotalCost"))
    print("="*77)
    for keyID in prodDict:
        totalCost = float(prodDict[keyID][1])*int(prodDict[keyID][2])
        print("{0:0}\t{1:10}\t\t${2:5.2f}\t{3:10}\t\t ${4:10.2f}".format(int(keyID),\
            prodDict[keyID][0], float(prodDict[keyID][1]), int(prodDict[keyID][2]),\
            float(totalCost)))
        grandTotal += totalCost
    print(" ")
    print("Grand Total: ${:.2f}".format(grandTotal))
    
def main():
    prodDict = {}
    fName = str(input("Enter the name of the file: "))
    while not os.path.isfile(fName):
        print("Error. The file", fName, "does not exist")
        fName = str(input("Enter the name of the file: "))
    openFile(prodDict, fName)
       
    mainOptionList=["Add product", "Sort by quantity (low to high)"\
            , "Print Inventory", "Quit"]
    menuStr = createMenu(mainOptionList, "Main Menu")
    choice = getValidChoice(len(mainOptionList), menuStr)

    while choice != 4:
        if choice == 1:
            addProduct(prodDict)
            choice = getValidChoice(len(mainOptionList), menuStr)
        elif choice == 2:
            sortByQuantity(prodDict)
            choice = getValidChoice(len(mainOptionList), menuStr)
        elif choice == 3:
            printReport(prodDict)
            choice = getValidChoice(len(mainOptionList), menuStr)
main()

