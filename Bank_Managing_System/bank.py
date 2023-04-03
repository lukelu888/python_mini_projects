"""
This is the Bank class with all functionalities implemented
"""
from account import Account


class Bank:

    def __init__(self, accountOffSet, accountLimit):
        self.accountOffSet = accountOffSet
        self.accountLimit = accountLimit
        self.availableAccountIDs = list(range(accountOffSet, accountOffSet + accountLimit))
        self.bankAccounts = {}

    @staticmethod
    def getYesNoAnswer() -> str:
        while (ans := input().strip().upper()) not in ('Y', 'N'):
            print("Error! Invalid input! Answer must be 'Y' or 'N'")
        return ans

    @staticmethod
    def getPositiveDecimal() -> float:
        while True:
            try:
                num = float(input("Enter a Positive Decimal number:"))
                if num > 0:
                    return num
                else:
                    print("Error! Invalid input! Input number must be greater than zero!")
            except ValueError as v:
                print(v)

    def prePopulateBankAccounts(self) -> None:
        self.availableAccountIDs.sort()
        self.bankAccounts.setdefault(self.availableAccountIDs[0], Account("luke", "lu", 1000.0))
        self.availableAccountIDs.pop(0)
        self.bankAccounts.setdefault(self.availableAccountIDs[0], Account("peter", "pan", 1000.0))
        self.availableAccountIDs.pop(0)
        self.bankAccounts.setdefault(self.availableAccountIDs[0], Account("jab", "jab", 2000.0))
        self.availableAccountIDs.pop(0)

    def printAccount(self, accountId: int) -> None:
        if accountId in self.bankAccounts:
            print(f"{'Account ID:':<20s} {'First Name:':<20s}{'Last Name:':<20s}{'Balance:':<20s}")
            print(f"{accountId:<20d}", self.bankAccounts[accountId])
        else:
            print(f"Account not found with ID {accountId}")

    def promptValidAccountId(self) -> int or None:
        while True:
            try:
                accountId = int(input("Enter Account ID: "))
                if accountId in self.bankAccounts.keys():
                    return accountId
                else:
                    print(f"Error! Invalid ID! Account with ID {accountId} dont exist!")
                    print("Do you want to try another time?(y/n):")
                    if Bank.getYesNoAnswer() == 'N':
                        return None
            except Exception as e:
                print(e)

    def addAccount(self) -> None:
        print("Option 1: Add a bank account:")
        if len(self.bankAccounts) < 100:
            while True:
                try:
                    first_name, last_name = input(
                        "plz enter your first name and last name seperate by comma:").strip().split(',')
                    if (0 < len(first_name) <= 20 and first_name.replace(" ", "").replace("-", "").isalpha()) and \
                            (0 < len(first_name) <= 20 and last_name.replace(" ", "").replace("-", "").isalpha()):
                        break
                    else:
                        raise ValueError(
                            "Error: Invalid input! "
                            "First Name and Last Name must be all letters(space and '-' are allowed)"
                            " and their lengths are 1-20 characters!")
                except ValueError as v:
                    print(v)

            while True:
                try:
                    accountBalance = float(input("plz enter your account start balance(greater than zero):"))
                    if accountBalance >= 0:
                        break
                    else:
                        raise ValueError(
                            "Error: Invalid input! Account balance must be non-negative!")
                except ValueError as v:
                    print(v)

            account = Account(first_name, last_name, accountBalance)

            self.availableAccountIDs.sort()
            accountId = self.availableAccountIDs[0]

            # self.bankAccounts[accountId] = account
            self.bankAccounts.setdefault(accountId, account)
            self.availableAccountIDs.pop(0)

            print("Success!Here is the account info you added:")
            self.printAccount(accountId)
        else:
            print(f"The maximum number of bank accounts - {self.accountLimit} is reached, cannot add a new one.")

    def removeAccount(self) -> None:
        print("Option 2: Remove a bank account:")
        if self.bankAccounts:
            accountId = self.promptValidAccountId()
            if accountId is not None:
                print("Here is the account info you want to remove:")
                self.printAccount(accountId)
                print("Do you confirm to remove this account? (y/n):")

                if Bank.getYesNoAnswer() == 'Y':
                    # del self.bankAccounts[accountId]
                    self.bankAccounts.pop(accountId)
                    self.availableAccountIDs.append(accountId)
                    print(f"Account with ID {accountId} has been removed!")
                else:
                    print("Operation canceled!")
        else:
            print("There's no account in the bank! Cannot delete!")

    def displayAccountInfo(self) -> None:
        print("Option 3: Display a bank account info:")
        if self.bankAccounts:
            accountId = self.promptValidAccountId()
            if accountId is not None:
                print("Here is the account info you want to display:")
                self.printAccount(accountId)
        else:
            print("There's no account in the bank! Cannot display!")

    def applyDepositIntoAccount(self) -> None:
        print("Option 4: Apply a deposit into account:")
        if self.bankAccounts:
            accountId = self.promptValidAccountId()
            if accountId is not None:
                print("To deposit an amount into your account, ", end="")
                amount = Bank.getPositiveDecimal()
                self.bankAccounts[accountId].balance += amount
                print(f"Success!You have deposited ${amount} into your account!")
                print("Here is your account info:")
                self.printAccount(accountId)
        else:
            print("There's no account in the bank! Cannot apply deposit!")

    def applyWithdrawFromAccount(self) -> None:
        print("Option 5: Apply a withdraw from account:")
        if self.bankAccounts:
            accountId = self.promptValidAccountId()
            if accountId is not None:
                while True:
                    print("To withdraw an amount from your account, ", end="")
                    amount = Bank.getPositiveDecimal()
                    if amount <= self.bankAccounts[accountId].balance:
                        self.bankAccounts[accountId].balance -= amount
                        print(f"Success!You withdrew ${amount} from your account!")
                        print("Here is your account info:")
                        self.printAccount(accountId)
                        break
                    else:
                        print("Not enough funds to withdraw!")
                        print("Do you want to try again?(y/n):")
                        if Bank.getYesNoAnswer() == 'N':
                            break
            else:
                print("There's no account in the bank! Cannot apply withdraw!")

    def sortAndDisplayAccount(self) -> None:
        print("Option 6: Sort and display accounts by balance, last name, first name:")
        if self.bankAccounts:
            print("Do you want to sort the client lists by Ascending order(Y) or Descending order(N)?(y/n):")
            ans = Bank.getYesNoAnswer()
            if ans == 'Y':
                sorted_bankAccounts = dict(sorted(self.bankAccounts.items(), key=(
                    lambda item: (item[1].balance, item[1].lastName, item[1].firstName))))
                print(
                    "Here is the sorted list of client accounts in ascending order (sort order: balance, last name, first name):")
                print(f"{'Account ID:':<20s} {'First Name:':<20s}{'Last Name:':<20s}{'Balance:':<20s}")
                for accountId, account in sorted_bankAccounts.items():
                    print(f"{accountId:<20d}", account)
            else:
                sorted_bankAccounts = dict(sorted(self.bankAccounts.items(), key=(
                    lambda item: (item[1].balance, item[1].lastName, item[1].firstName)), reverse=True))
                print(
                    "Here is the sorted list of client accounts in descending order (sort order: balance, last name, first name):")
                print(f"{'Account ID:':<20s} {'First Name:':<20s}{'Last Name:':<20s}{'Balance:':<20s}")
                for accountId, account in sorted_bankAccounts.items():
                    print(f"{accountId:<20d}", account)
        else:
            print("There's no account in the bank! Cannot sort!")

    def displayAverageBalance(self) -> None:
        print("Option 7: Display the average balance of all the accounts:")
        avg_balance = sum([account.balance for account in self.bankAccounts.values()]) / len(self.bankAccounts)
        print(f"The average balance of all the accounts is ${avg_balance:.2f}")

    def displayTotalBalance(self) -> None:
        print("Option 8: Display the total balance of all the accounts:")
        total_balance = sum([account.balance for account in self.bankAccounts.values()])
        print(f"The total balance of all the accounts is ${total_balance:.2f}")
