import ZODB, ZODB.config
import persistent
from abc import ABC, abstractclassmethod
from datetime import date
from datetime import datetime
path = "./config.xml"
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root
now = datetime.now()
today = date.today()

class Customer(persistent.Persistent):
    def __init__(self,name = ""):
        self.name = name
        self.accounts = persistent.list.PersistentList()

    def __str__(self):
        return str(self.name)
    
    def setName(self,n):
        self.name = n

    def addAccount(self,a):
        self.accounts.append(a)
        return a
    
    def getAccount(self, n):
        if 0<= n < len(self.accounts):
            return self.accounts[n]
        return None
    
    def printStatus(self):
        print(self.__str__())
        for a in self.accounts:
            print("", end="")
            a.printStatus()

class Account(ABC):
    def __init__(self,balance = 0.0, owner = None):
        self.balance = balance
        self.owner = owner
        self.bankTransaction = persistent.list.PersistentList()

    @abstractclassmethod
    def __str__(self):
        raise NotImplementedError('user must define')
    
    def deposit(self,m):
        self.balance += m
        self.bankTransaction.append(BankTransaction(m,self.balance-m,self.balance,str(today)+str(now),"deposit"))

    def printTransaction(self):
        for a in self.bankTransaction:
            print("", end="")
            a.printDetail()
        
    def withdraw(self,m):
        self.balance -= m
        self.bankTransaction.append(BankTransaction(m,self.balance+m,self.balance,str(today)+str(now),"withdraw"))

    def transferIn(self,m,o):
        self.balance += m
        self.bankTransaction.append(BankTransaction(m,self.balance-m,self.balance,str(today)+str(now),"transfer from "+ str(self.owner)))


    def transfer(self,m,o):
        self.balance -= m
        o.transferIn(m,o)
        self.bankTransaction.append(BankTransaction(m,self.balance+m,self.balance,str(today)+str(now),"transfer to "+ str(o.owner)))

    def accountDetail(self):
        return "Account name : " + str(self.owner) + " balance : " + str(self.balance)
    
    def getBalance(self):
        return self.balance 

    @abstractclassmethod
    def printStatus(self):
        pass

class SavingAccount(Account, persistent.Persistent):
    def __init__(self, balance=0, owner=None):
        self.interest = 1
        Account.__init__(self, balance, owner)

    def printStatus(self):
        print("Saving Account of Customer name : " + str(self.owner) + " balance : " + str(self.balance) +" Interest : "+ str(self.interest))

    def withdraw(self, m):
        if self.balance<m:
            return False
        self.balance -= m
        self.bankTransaction.append(BankTransaction(m,self.balance+m,self.balance,str(today)+str(now),"withdraw"))
        
    
class CurrentAccount(Account, persistent.Persistent):
    def __init__(self, balance ,owner):
        self.limit = -5000.00
        Account.__init__(self, balance, owner)
    
    def withdraw(self,m):
        if self.balance-m < self.limit:
            return False
        self.balance-=m
        self.bankTransaction.append(BankTransaction(m,self.balance+m,self.balance,str(today)+str(now),"withdraw"))

    def printStatus(self):
        print("Current Account of Customer name : " + str(self.owner) + " balance : " + str(self.balance) + " Limit : "+ str(self.limit))


class BankTransaction(persistent.Persistent):
    def __init__(self,amount,old_balance,new_balance,timestamp,ttype):
        self.amount = amount
        self.old_balance = old_balance
        self.new_balance = new_balance
        self.timestamp = timestamp
        self.ttype = ttype

    def printDetail(self):
        print(self.ttype+"\n")
        print("Amount: "+str(self.amount)+"\n")
        print("Oldbalance: "+str(self.old_balance)+"\n")
        print("NEwbalance: "+str(self.new_balance)+"\n")
        print("Timestamp: "+str(self.timestamp)+"\n")