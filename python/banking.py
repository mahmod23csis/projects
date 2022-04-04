__author__="Mahmod Ahmad"

"""This is a banking program that lets the user choose from a list
from the main menu. If the user chooses Savings, then it shows
another menu called Savings Menu where the user can view the interest
and savings balance. When the user selects Checking, another
menu pops up where the user can deposit, withdraw, or display
the checking balance. Finally, when the user enters 3, the 
program ends."""

def createMenu(listOfChoices, menuTitle):
    menuStr=menuTitle
    for n in range(len(listOfChoices)):
        menuStr+="\n"+str(n+1)+". "+listOfChoices[n]
    return menuStr

def getValidChoice(numChoices, menuStr):
        print(menuStr)
        choice = input("Select a choice: ")
        while choice.isdigit()==False or int(choice) > numChoices \
              or int(choice) < 1:
            print("Invalid choice. Please try again!")
            print(menuStr)
            choice = input("Select choice: ")
        return int(choice)

def handleCheckMenu(checkBal, numChoices, checkMenuStr):
    chkCh = getValidChoice(numChoices, checkMenuStr)
    while chkCh != numChoices:
        if chkCh == 1:
            checkBal = deposit(checkBal)
        elif chkCh == 2:
            checkBal = withdrawal(checkBal)
        elif chkCh == 3:
            print("Your current balance is: $", checkBal)
            
        chkCh = getValidChoice(numChoices, checkMenuStr)
    return checkBal

def handleSavings(savBal, numChoices, saveMenuStr):
    savCh = getValidChoice(numChoices, saveMenuStr)
    while savCh != numChoices:
        if savCh == 1:
            savBal = showInterestEarned(savBal)
        elif savCh == 2:
            print("Your savings balance is: $", savBal)
        savCh = getValidChoice(numChoices, saveMenuStr)
    return savBal
    
def deposit(checkBal):
    amt = float(input("Enter an amount to deposit: "))
    checkBal += amt
    print("$", amt, "has been deposited to your account.")
    print("Your current balance is: $", checkBal)
    return checkBal

def withdrawal(checkBal):
    amt = float(input("Enter an amount to wathdraw: "))
    if (checkBal - amt) >= 0:
        checkBal -= amt
        print("$", amt, "has been withdrawed from your account.")
        print("Your current balance is: $", checkBal)
    else:
        print("Insufficient funds.")
    return checkBal

def showInterestEarned(savBal):
    savBal += (2*savBal/100)
    print("Your savings after interest is: $", savBal)
    return savBal

def main():
    checkBal = 0; savBal = 100

    savOptionList = ["Display Interest Earned", "Display Savings Balance",
                     "Back to Main"]
    chkOptionList = ["Deposit", "Withdrawal", "Display Checking Balance",
                      "Back to Main"]
    mainOptionList = ["Savings", "Checking", "Quit"]
    menuStr = createMenu(mainOptionList, "Main Menu")
    choice = getValidChoice(len(mainOptionList), menuStr)

    saveMenuStr = createMenu(savOptionList, "Savings Menu")
    checkMenuStr = createMenu(chkOptionList, "Checking Menu")

    while choice != 3:
        if choice == 1:
            savBal = handleSavings(savBal, len(savOptionList), saveMenuStr)
            choice = getValidChoice(len(mainOptionList), menuStr)
        elif choice == 2:
            checkBal = handleCheckMenu(checkBal, len(chkOptionList), checkMenuStr)
            choice = getValidChoice(len(mainOptionList), menuStr)
main()
