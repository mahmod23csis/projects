__author__="Mahmod Ahmad"
__date__="10/13/2020"

"""This program counts the frequency of each word given from a text file.
It cleans the text from any punctuation. Then it gives options to choose from.
The user can add a new word, check if a word exists, delete
a word from the dictionary or print the entire dictionary."""

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
        
def cleanData(lineList):
    punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    noPunc = ""
    for line in lineList :
        if line == '\n':
            line = line.replace('\n', ' ')
        if line not in punc:
            noPunc += line
    return noPunc

def cleanDict(word):
    word = word.lower()
    wordList = word.split()
    wordDict ={ }
    for chars in wordList:
        if chars not in wordDict:
            wordDict[chars] = 0
        wordDict[chars] += 1
    return wordDict

def printReport(myDict):
    print(" ")
    print("{:<20} {:<20}".format("Words", "Frequency"))
    print("="*30)
    for k in sorted(myDict.keys()):
        print("{:<20} {:<20}".format(k, myDict[k]))
    print(" ")
        
def addToDict(newWord, myDict):
    if newWord.lower() not in myDict:
        myDict[newWord.lower()] = 0
    myDict[newWord.lower()] += 1
    print(newWord.lower(), "is added to Dictionary.")

def checkWord(word, myDict):
    if word.lower() in myDict:
        print(word.lower(), "is already in Dictionary")
    else:
        print(word.lower(), "is not in dictionary")

def deleteWord(word, myDict):
    if word.lower() in myDict:
        myDict.pop(word.lower())
        print(word.lower(), "is deleted from Dictionary.")
    else:
        print(word.lower(), "is not in Dictionary.")

def main():
    fName = str(input("Enter the name of the file: "))
    while not os.path.isfile(fName):
        print("Error. The file", fName, "does not exist.")
        fName = str(input("Enter the name of the file: "))
    fObj = open(fName,"r")
    lineList = fObj.read()
    cleanD = cleanData(lineList)
    myDict = cleanDict(cleanD)
    fObj.close()

    mainOptionList=["Add", "Check", "Delete", "Print", "Quit"]
    menuStr = createMenu(mainOptionList, "Main Menu")
    choice = getValidChoice(len(mainOptionList), menuStr)

    while choice != 5:
        if choice == 1:
            wordToadd = input("Enter a new word to be added: ")
            addToDict(wordToadd, myDict)
            choice = getValidChoice(len(mainOptionList), menuStr)
        elif choice == 2:
            wordTocheck = input("Enter a word to check if it is in Dictionary: ")
            checkWord(wordTocheck, myDict)
            choice = getValidChoice(len(mainOptionList), menuStr)
        elif choice == 3:
            wordTodelete = input("Enter a word to delete from Dictionary: ")
            deleteWord(wordTodelete, myDict)
            choice = getValidChoice(len(mainOptionList), menuStr)
        elif choice == 4:
            printReport(myDict)
            choice = getValidChoice(len(mainOptionList), menuStr)
main()
