__author__="Mahmod Ahmad"
__date__="11/06/2020"

"""This program creates a class called Account and uses a list to store
its attributes. It automatically assigns a new Account ID to the customer.
It also calculates interest for Checking and Savings accounts"""

class Account:
    __nextAcctID = 1000

    def __init__(self, tmpBank, tmpType, tmpBalance):
        AcctID = Account.__setAcctID()
        self.__listCustInfo = [AcctID, tmpBank, tmpType, tmpBalance]

    def getAcctID(self):
        return self.__listCustInfo[0]
    
    def __setAcctID():
        id = Account.__getnextAcctID()
        Account.__nextAcctID += 10
        return id
    
    def __getnextAcctID():
        return Account.__nextAcctID

    def getBank(self):
        return self.__listCustInfo[1]
    
    def setBank(self, newBank):
        self.__listCustInfo[1] = newBank
    
    def getType(self):
        return self.__listCustInfo[2]
    
    def getBalance(self):
        return self.__listCustInfo[3]
    
    def setBalance(self, newBalance):
        self.__listCustInfo[3] = newBalance
    
    def __str__(self):
        id = int(self.getAcctID())
        bank = str(self.getBank())
        bankType = str(self.getType())
        balance = float(self.getBalance())
        tmp = "Account #:{:5}\nBank: {:10s}\nAccount Type:\
 {:7s}\nBalance: ${:<7.2f}".format (id, bank, bankType, balance)
        return tmp
    
    def calcInterest(self):
        if self.__listCustInfo[2] == "Checking":
            interest = float(self.__listCustInfo[3] * 0.01)
            balanceInt = interest + self.getBalance()
            self.setBalance(balanceInt)
        elif self.__listCustInfo[2] == "Savings":
            interest = float(self.__listCustInfo[3] * 0.02)
            balanceInt = interest + self.getBalance()
            self.setBalance(balanceInt)
