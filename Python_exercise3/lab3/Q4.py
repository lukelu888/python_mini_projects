"""
Yinglin Lu 2212059
class encapsulation/properties/Inheritance/method overriding/chaining
Nov 12, 2022
This is Q4
"""


class Account:
    def __init__(self, balance=0):
        self.__balance = 0
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print(
                "cannot assign negative value to balance! balance will be unchanged or set to zero for first-time setup!")
        else:
            self.__balance = value

    def credit(self, amount):
        print(f"You want to credit ${amount} to your account:")
        if amount < 0:
            print("Cannot credit negative amount, balance will be unchanged!")
            return False
        else:
            self.balance += amount
            print("Credit Operation Success!")
            return True

    def debit(self, amount):
        print(f"You want to debit ${amount} to your account:")
        if 0 <= amount <= self.balance:
            self.balance -= amount
            print("Debit Operation Success!")
            return True
        else:
            print("cannot debit negative amount or amount exceeded account balance, balance will be unchanged!")
            return False

    def __repr__(self):
        return (f"Account balance: ${self.balance:.2f}")


class SavingAccount(Account):
    def __init__(self, balance=0, interestRate=0.0):
        super().__init__(balance)
        self.__interestRate = interestRate

    @property
    def interestRate(self):
        return self.__interestRate

    @interestRate.setter
    def interestRate(self, value):
        if value < 0:
            print(
                "cannot assign negative value to interestRate! interestRate will be unchanged or set to zero for first-time setup!")
        else:
            self.__interestRate = value

    def calculateAnnualInterest(self):
        return self.balance * self.interestRate / 100

    def __repr__(self):
        return f"Saving Account balance: ${self.balance:<20.2f} Current Interest rate: {self.interestRate:.2f}% "


class CheckingAccount(Account):
    def __init__(self, balance=0, transactionFee=0.0):
        super().__init__(balance)
        self.__transactionFee = transactionFee

    @property
    def transactionFee(self):
        return self.__transactionFee

    @transactionFee.setter
    def transactionFee(self, value):
        if value < 0:
            print(
                "cannot assign negative value to transactionFee! transactionFee will be unchanged or set to zero for "
                "first-time setup!")
        else:
            self.__transactionFee = value

    def __repr__(self):
        return f"Checking Account balance: ${self.balance:<20.2f} Current Transaction Fee: ${self.transactionFee:.2f}"

    def credit(self, value):
        if super().credit(value):
            self.balance -= self.transactionFee
        else:
            print("Operation cancelled!")

    def debit(self, amount):
        if super().debit(amount):
            self.balance -= self.transactionFee
        else:
            print("Operation cancelled!")


account = Account(100)
checkingAccount = CheckingAccount(100, 2.0)
savingAccount = SavingAccount(100, 2.5)

for ac in (account, checkingAccount, savingAccount):
    print("Current", ac)
    ac.debit(20)
    print("Current", ac)
    creditAmount = 20
    if ac is savingAccount:
        creditAmount = ac.calculateAnnualInterest()
        print("This is the annual interest you earned: $", creditAmount, "and it will be credited to your account!")

    ac.credit(creditAmount)
    print("Current", ac, "\n\n")
