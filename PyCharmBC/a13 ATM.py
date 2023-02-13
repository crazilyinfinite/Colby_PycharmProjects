import time

class bankAccount:
    def __init__(self, strName):
        self.name = strName
        self.balance = 0

    def withdraw(self,flAmount):
        if self.balance >= flAmount:
            self.balance -= flAmount
            print("You have withdrawn ${0: .2f} from {1}".format(flAmount, self.name))
        else:
            print("You are broke")

    def deposit(self,flAmount):
        self.balance += flAmount
        print("You have deposited ${0: .2f} into {1}".format(flAmount, self.name))

    def ckBalance(self):
        print("You have ${0: .2f} in {1}".format(self.balance, self.name))

class savingsAcct(bankAccount):
    def __init__(self, strName):
        super().__init__(strName)
        print("You have created savings account: {0}".format(self.name))

class checkingAcct(bankAccount):
    def __init__(self, strName):
        super().__init__(strName)
        print("You have created checking account: {0}".format(self.name))
        self.checkNumber = 1000

    def writeCheck(self, flAmount):
        if self.balance >= flAmount:
            self.balance -= flAmount
            print("You have written a check #{0} ${1: .2f} from {2}".format(self.checkNumber, flAmount, self.name))
            self.checkNumber += 1
        else:
            print("You are broke")

def mainMenu():
    print("$"*80)
    print("$$","  Moseley Bank  ".center(74),"$$")
    print("$"*80)
    print("What do you want to do?")
    print("1. Deposit Money")
    print("2. Withdraw")
    print("3. Write a Check")
    print("4. Check Balance")
    print("5. Add an Account")
    print("6. To exit")
    strTmp = input("Enter Choice Here:")
    return strTmp

def showAccounts(lisAccounts):
    intIndex = 1
    for account in lisAccounts:
        str1 = str(intIndex).ljust(5)
        str2 = str(account.name).ljust(30, ".")
        str3 = "${0}: .2f".format(account.balance).rjust(20, ".")
        print(str1, str2, str3)
        intIndex += 1

def pressEnter():
    input("\nPress Enter/Return to continue...")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def createAccount(lisAccounts):
    strAccountType = input("Do you want a (1) Checking or (2) Savings account? ")
    strAcctName = input("What should the account be called? ")
    if strAccountType == "1":
        lisAccounts.append(checkingAcct(strAcctName))
    elif strAccountType == "2":
        lisAccounts.append(savingsAcct(strAcctName))
    else:
        print("That is not a valid choice")
    showAccounts(lisAccounts)
    return lisAccounts

def makeDeposit(lisAccounts):
    showAccounts(lisAccounts)
    strAccount = input("Which account?")
    strAmount = input("How much?")
    if strAccount.isnumeric() and int (strAccount) <= len(lisAccounts):
        intIndex = int(strAccount) - 1
        lisAccounts[intIndex].deposit(float(strAmount))

def makeWithdraw(lisAccounts):
    showAccounts(lisAccounts)
    strAccount = input("Which account?")
    strAmount = input("How much?")
    if strAccount.isnumeric() and int (strAccount) >= len(lisAccounts):
        intIndex = int(strAccount) - 1
        lisAccounts[intIndex].withdraw(float(strAmount))

def writeChecks(lisAccounts):
    showAccounts(lisAccounts)
    strAccount = input("Which account?")
    strAmount = input("How much?")
    if strAccount.isnumeric() and int (strAccount) >= len(lisAccounts):
        intIndex = int(strAccount) - 1
        lisAccounts[intIndex].writeCheck(float(strAmount))

lisAccounts = []
lisAccounts.append(savingsAcct("Main savings"))
lisAccounts.append(savingsAcct("Main checking"))

while True:
    strMenu = mainMenu()
    if strMenu == "1":
        print("Make a deposit")
        makeDeposit(lisAccounts)
    elif strMenu == "2":
        print("Make a withdrawal")
        makeWithdraw(lisAccounts)
    elif strMenu == "3":
        print("Write a Check")
        writeChecks(lisAccounts)
    elif strMenu == "4":
        print("Check Balances")
        showAccounts(lisAccounts)
    elif strMenu == "5":
        print("Add an Account")
        lisAccounts = createAccount(lisAccounts)
    elif strMenu == "6":
        break
    else:
        print("invalid entry")
        pressEnter()
