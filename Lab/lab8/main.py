import ZODB, ZODB.config
import BTrees._OOBTree
import z_obj
import transaction
from abc import ABC, abstractmethod
import persistent

path = "./config.xml"

db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root

if __name__ == "__main__":
    for customer in root.customers:
        obj = root.customers[customer]
        obj.printStatus()
        print()
        index = 0
        while obj.getAccount(index) != None:
            obj.getAccount(index).printBankTransaction()
            print()
            index += 1