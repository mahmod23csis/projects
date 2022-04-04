__author__="Mahmod Ahmad"
__date__="11/06/2020"

"""Testing getters, setters and the string function"""

from modAccountV3 import *

def main():
    #Testing getters
    a1 = Account("Gate City Bank", "Checking", 150.98)
    print(a1)
    a1.calcInterest()
    print("Interest Checking Account: $" + str(a1.getBalance()))
    print("")

    a2 = Account("Bell Bank", "Savings", 350.89)
    print(a2)
    a2.calcInterest()
    print("Interest Savings Account: $" + str(a2.getBalance()))
    print("")
    #Testing setters
    a2.setBank("Wells Fargo")
    a2.setBalance(279.67)
    print(a2)
    a2.calcInterest()
    print("Interest Savings Account: $" + str(a2.getBalance()))
main()
