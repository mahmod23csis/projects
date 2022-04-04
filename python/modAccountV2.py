__author__="Mahmod Ahmad"
__date__="11/06/2020"

"""This program creates a class called Account. It automatically
assigns a new Account ID to the customer. It also calculates interest
for Checking and Savings accounts"""

class Account:
    __nextAcctID = 1000

    def __init__(self, tmpBank, tmpType, tmpBalance):
        self.__AcctID = Account.__setAcctID()
        self.__bank = tmpBank
        self.__type = tmpType
        self.__balance = tmpBalance

    def getAcctID(self):
        return self.__AcctID
    
    def __setAcctID():
        id = Account.__getnextAcctID()
        Account.__nextAcctID += 10
        return id
    
    def __getnextAcctID():
        return Account.__nextAcctID

    def getBank(self):
        return self.__bank
    
    def setBank(self, newBank):
        self.__bank = newBank
    
    def getType(self):
        return self.__type
    
    def getBalance(self):
        return self.__balance
    
    def setBalance(self, newBalance):
        self.__balance = newBalance
    
    def __str__(self):
        id = int(self.getAcctID())
        bank = str(self.getBank())
        bankType = str(self.getType())
        balance = float(self.getBalance())
        tmp = "Account #:{:5}\nBank: {:10s}\nAccount Type:\
 {:7s}\nBalance: ${:<7.2f}".format (id, bank, bankType, balance)
        return tmp
    
    def calcInterest(self):
        if self.__type == "Checking":
            interest = float(self.getBalance() * 0.01)
            balanceInt = interest + self.getBalance()
            self.setBalance(balanceInt)
        elif self.__type == "Savings":
            interest = float(self.getBalance() * 0.02)
            balanceInt = interest + self.getBalance()
            self.setBalance(balanceInt)
