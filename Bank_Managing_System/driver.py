"""
Bank  Managing System
Nov 7, 2022
This is where the Project start
"""
# print(__doc__)

from bank import Bank

ACCOUNT_OFFSET = 10_000
ACCOUNT_LIMIT = 100
bank = Bank(ACCOUNT_OFFSET, ACCOUNT_LIMIT)
bank.prePopulateBankAccounts()


def func(i: int) -> None:
    case = {1: bank.addAccount,
            2: bank.removeAccount,
            3: bank.displayAccountInfo,
            4: bank.applyDepositIntoAccount,
            5: bank.applyWithdrawFromAccount,
            6: bank.sortAndDisplayAccount,
            7: bank.displayAverageBalance,
            8: bank.displayTotalBalance,
            9: lambda: print("Thank you for using banking system! GoodBye!\n\n")}

    fun = case.get(i, lambda: print("Invalid choice!"))

    return fun()


def main():
    choice = 0
    while choice != 9:
        print("\n\n\t\tMenu Options\n" +
              "*********************************************************************************************************************************\n" +
              "1.Add a bank account.\n" +
              "2.Remove a bank account.\n" +
              "3.Display account information(by account number).\n" +
              "4.Make a deposit(by account number).\n" +
              "5.Make a withdraw(by account number).\n" +
              "6.Sort and display the list of clients according to their balance, family name and given name, in ascending or descending order.\n" +
              "7.Display the average balance value of the accounts.\n" +
              "8.Display the total balance value of the accounts.\n" +
              "9.Exit the application.\n" +
              "***********************************************************************************************************************************")

        while True:
            try:
                choice = int(input("Please enter your choice(1-9):"))
                if 1 <= choice <= 9:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Error:Invalid Input! Input must be a number 1-9!")

        func(choice)

if __name__ == '__main__':
    main()
