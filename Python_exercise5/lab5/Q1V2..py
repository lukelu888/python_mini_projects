import random


def toWord(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if num == 0:
        return "zero"
    elif num < 20:
        return ones[num]
    elif num < 100:
        return tens[num // 10] + " " + toWord(num % 10)
    elif num < 1000:
        return toWord(num // 100) + " hundred " + toWord(num % 100)
    elif num < 1_000_000:
        return toWord(num // 1000) + " thousand " + toWord(num % 1000)
    elif num < 1_000_000_000:
        return toWord(num // 1_000_000) + " million " + toWord(num % 1_000_000)
    elif num < 1_000_000_000_000:
        return toWord(num // 1_000_000_000) + " billion " + toWord(num % 1_000_000_000)
    else:
        return f"{num:<_d} is too large, i dont know the english word after billion!"


def createYourOwnExample():
    while not (num := input("enter an positive integer:").strip()).isdigit():
        print("error! must be positive int")
    print(f"input:{int(num):<_d}, output: {toWord(int(num))}\n\n")


def createRandomExample():
    num = random.randint(0, (1_000_000_000_000 - 1))
    print(f"input:{num:<_d}, output: {toWord(num)}\n\n")


def menu():
    print("[0]- exit")
    print("[1]- Exemple: 123")
    print("[2]- Exemple: 12345")
    print("[3]- Exemple: 1234567")
    print("[4]- Exemple: 1234567891")
    print("[5]- Enter your own example:")
    print("[6]- create random example:")


def func(i):
    case = {'0': lambda: print("Good Bye!"),
            '1': lambda: print(f"input:{123:<_d}, output: {toWord(123)}\n\n"),
            '2': lambda: print(f"input:{12345:<_d}, output: {toWord(12345)}\n\n"),
            '3': lambda: print(f"input:{1234567:<_d}, output: {toWord(1234567)}\n\n"),
            '4': lambda: print(f"input:{1234567891:<_d}, output: {toWord(1234567891)}\n\n"),
            '5': createYourOwnExample,
            '6': createRandomExample
            }
    fun = case.get(i, lambda: print("invalid choice! choice must be from 0 to 6\n\n"))
    return fun()


def main():
    choice = '-1'

    while choice != '0':
        menu()
        while not (choice := input("enter your choice:").strip()).isdigit():
            print("error! input must be positive int")
        func(choice)


main()
