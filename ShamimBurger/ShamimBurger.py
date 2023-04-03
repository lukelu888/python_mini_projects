rollTypes = ["White", "Brown rye"]
meats = ["Sausage", "Bacon", "Sausage&bacon"]
additions = {"Tomato": 0.27, "Lettuce": 0.75, "Cheese": 1.13, "Egg": 5.43, "Lentils": 3.41, "pickle": 0.15}
sides = {"Chips": 2.75, "Drink": 1.81}


class Hamburger:
    def __init__(self, rollType, meat, basePrice):
        self.rollType = rollType
        self.meat = meat
        self.basePrice = basePrice
        self.name = "Basic Hamburger"

    def __repr__(self):
        return f"{self.name} on a {self.rollType} roll with {self.meat}, price is ${self.basePrice}"

    def addAdditions(self, choices):
        sum = 0
        for choice in choices:
            print(f"Added {choice} for an extra ${additions[choice]}")
            sum += additions[choice]
        return sum

    def totalPrice(self, choices):
        if len(choices) <= 4:
            total = self.basePrice + self.addAdditions(choices)
            print(f"Total {self.name} price is ${total}")
        else:
            print("can choose maximum 4 toppings")


class HealthyBurger(Hamburger):
    def __init__(self, meat, basePrice):
        super().__init__("Brown rye", meat, basePrice)
        self.name = "Healthy Burger"

    def __repr__(self):
        return f"{self.name} on a {self.rollType} roll with {self.meat}, price is ${self.basePrice}"

    def totalPrice(self, choices):
        if len(choices) <= 6:
            total = self.basePrice + self.addAdditions(choices)
            print(f"Total {self.name} price is ${total}")
        else:
            print("can choose maximum 6 toppings")


class DeluxeBurger(Hamburger):
    def __init__(self, rollType, meat, basePrice):
        super().__init__(rollType, meat, basePrice)
        self.name = "DeluxeBurger"

    def __repr__(self):
        return f"{self.name} on a {self.rollType} roll with {self.meat}, price is ${self.basePrice}"

    def addSides(self, choices):
        sum = 0
        for choice in choices:
            print(f"Added {choice} for an extra ${sides[choice]}")
            sum += sides[choice]
        return sum

    def totalPrice(self, choices):

        if DeluxeBurger.validateChoices(choices):
            total = self.basePrice + self.addSides(choices)
            print(f"Total {self.name} price is ${total}")

    @staticmethod
    def validateChoices(choices):
        for choice in choices:
            if choice not in sides:
                print("Cannot add additional items to a deluxe burger, only drink and chips!")
                return False
        return True


def makeHamburger():
    print("what breadroll would you like\n"
          "[1]-White\n"
          "[2]-Brown rye\n")
    while True:
        try:
            rollChoice = int(input("Please enter your choice(1-2):"))
            if 1 <= rollChoice <= 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Error:Invalid Input! Input must be a number 1-2!")
    rollType = rollTypes[rollChoice - 1]

    print("What meat would you like\n"
          "[1]-Sausage\n"
          "[2]-bacon\n"
          "[3]-Sausage&bacon\n")
    while True:
        try:
            meatChoice = int(input("Please enter your choice(1-3):"))
            if 1 <= meatChoice <= 3:
                break
            else:
                raise ValueError
        except ValueError:
            print("Error:Invalid Input! Input must be a number 1-3!")

    meat = meats[meatChoice - 1]

    count_addition = 0
    ans = 'Y'
    additionChoices = {'1': "Tomato", '2': "Lettuce", "3": "Cheese", '4': "Egg", '5': "Lentils", '6': "pickle"}
    chosenAdditions = []
    while count_addition < 4 and ans == 'Y':
        print("what additions do you like\n"
              "[1]-Tomato:0.27\n"
              "[2]-Lettuce:0.75\n"
              "[3]-Cheese:1.13\n"
              "[4]-Egg:5.43\n"
              "[5]-Lentils:3.41\n"
              "[6]-pickle:0.15\n")
        while True:
            try:
                additionChoice = int(input("Please enter your choice(1-6):"))
                if 1 <= additionChoice <= 6:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Error:Invalid Input! Input must be a number 1-6!")

        chosenAdditions.append(additionChoices[str(additionChoice)])

        while (ans := input("Do you want another addition?").strip().upper()) not in ('Y', 'N'):
            print("Error! Invalid input! Answer must be 'Y' or 'N'")
        count_addition += 1
        if count_addition >= 4:
            print("you can choose max 4 additions!")

    b = Hamburger(rollType, meat, 3.56)
    print(b)
    b.totalPrice(chosenAdditions)


def makeHealthyBurger():
    print("What meat would you like\n"
          "[1]-Sausage\n"
          "[2]-bacon\n"
          "[3]-Sausage&bacon\n")
    while True:
        try:
            meatChoice = int(input("Please enter your choice(1-3):"))
            if 1 <= meatChoice <= 3:
                break
            else:
                raise ValueError
        except ValueError:
            print("Error:Invalid Input! Input must be a number 1-3!")

    meat = meats[meatChoice - 1]

    count_addition = 0
    ans = 'Y'
    additionChoices = {'1': "Tomato", '2': "Lettuce", "3": "Cheese", '4': "Egg", '5': "Lentils", '6': "pickle"}
    chosenAdditions = []
    while count_addition < 6 and ans == 'Y':
        print("what additions do you like\n"
              "[1]-Tomato:0.27\n"
              "[2]-Lettuce:0.75\n"
              "[3]-Cheese:1.13\n"
              "[4]-Egg:5.43\n"
              "[5]-Lentils:3.41\n"
              "[6]-pickle:0.15\n")
        while True:
            try:
                additionChoice = int(input("Please enter your choice(1-6):"))
                if 1 <= additionChoice <= 6:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Error:Invalid Input! Input must be a number 1-6!")

        chosenAdditions.append(additionChoices[str(additionChoice)])

        while (ans := input("Do you want another addition?").strip().upper()) not in ('Y', 'N'):
            print("Error! Invalid input! Answer must be 'Y' or 'N'")
        count_addition += 1
        if count_addition >= 6:
            print("you can choose max 4 additions!")

    h = HealthyBurger(meat, 5.67)
    print(h)
    h.totalPrice(chosenAdditions)


def makeDeluxeBurger():
    print("what breadroll would you like\n"
          "[1]-White\n"
          "[2]-Brown rye\n")
    while True:
        try:
            rollChoice = int(input("Please enter your choice(1-2):"))
            if 1 <= rollChoice <= 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Error:Invalid Input! Input must be a number 1-2!")
    rollType = rollTypes[rollChoice - 1]

    print("What meat would you like\n"
          "[1]-Sausage\n"
          "[2]-bacon\n"
          "[3]-Sausage&bacon\n")
    while True:
        try:
            meatChoice = int(input("Please enter your choice(1-3):"))
            if 1 <= meatChoice <= 3:
                break
            else:
                raise ValueError
        except ValueError:
            print("Error:Invalid Input! Input must be a number 1-3!")

    meat = meats[meatChoice - 1]

    ans = 'Y'
    sideChoices = {'1': "Chips", '2': "Drink"}
    chosenSides = []
    while ans == 'Y':
        print("what sides do you like\n"
              "[1]-Chips:2.75\n"
              "[2]-Drink:1.81\n"
              )
        while True:
            try:
                additionChoice = int(input("Please enter your choice(1-2):"))
                if 1 <= additionChoice <= 2:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Error:Invalid Input! Input must be a number 1-2!")

        chosenSides.append(sideChoices[str(additionChoice)])

        while (ans := input("Do you want another addition?").strip().upper()) not in ('Y', 'N'):
            print("Error! Invalid input! Answer must be 'Y' or 'N'")

    d = DeluxeBurger(rollType, meat, 14.54)
    print(d)
    d.totalPrice(chosenSides)


def main():
    choice = '0'
    while choice != '4':
        print("\n\n++++++++++ Menu ++++++++++++\n"
              "[1]-Hamburger 3.56\n"
              "[2]-HealthyBurger 5.67\n"
              "[3]-DeluxeBurger 14.54\n"
              "[4]-Exit\n")

        menu = {"1": makeHamburger, "2": makeHealthyBurger, "3": makeDeluxeBurger, '4': lambda :print("GoodBye")}
        while True:
            try:
                choice = input("Please enter your choice(1-4):")
                if 1 <= int(choice) <= 4:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Error:Invalid Input! Input must be a number 1-4!")

        func = menu.get(choice, lambda: print("Invalid choice!"))
        func()

main()

# b = Hamburger("White", "Sausage", 3.56)
# print(b)
# b.totalPrice("Tomato", "Cheese")
#
# h = HealthyBurger("Bacon", 5.67)
# print(h)
# h.totalPrice("Egg", "Lentils")
#
# d = DeluxeBurger("White", "Sausage&Bacon", 14.54)
# print(d)
# d.totalPrice("Chips", "Drink")
