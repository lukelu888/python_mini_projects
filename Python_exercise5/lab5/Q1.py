import random

base_word = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight",
             "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen",
             "15": "fifteen", "16": "sixteen", "17": "sixteen", "18": "eighteen", "19": "nineteen", "20": "twenty",
             "30": "thirty", "40": "forty", "50": "fifty", "60": "sixty", "70": "seventy", "80": "eighty",
             "90": "ninety"}


def toEnglishLessThan1000(num):
    word = ""
    if num == "0":
        word += "zero"
    elif num in base_word:
        word += base_word[num]
    else:
        if str(int(num[-2:])) in base_word:
            word += base_word[str(int(num[-2:]))]
        elif str(int(num[-2:])) != '0':
            word += base_word[(num[-2] + "0")] + " " + base_word[num[-1]]

    if 100 <= int(num) <= 999:
        word = base_word[num[-3]] + " hundred " + word

    return word


def toEnglishLessThanOneMillionGreaterThan1000(num):
    word = ""
    if int(num[-3:]) != 0:
        word += toEnglishLessThan1000(num[-3:])
    word = toEnglishLessThan1000(num[:-3]) + " thousand " + word
    return word


def toEnglishLessThanOneBillionGreaterThanOneMillion(num):
    word = ""
    if int(num[-6:]) != 0:
        word += toEnglishLessThanOneMillionGreaterThan1000(num[-6:])
    word = toEnglishLessThan1000(num[:-6]) + " million " + word
    return word


def toEnglishGreaterThanOneBillion(num):
    word = ""
    if int(num[-9:]) != 0:
        word += toEnglishLessThanOneBillionGreaterThanOneMillion(num[-9:])
    word = toEnglishLessThan1000(num[:-9]) + " billion " + word
    return word


def numToEnglish(num):
    if len(num) < 4:
        word = toEnglishLessThan1000(num)
    elif len(num) < 7:
        word = toEnglishLessThanOneMillionGreaterThan1000(num)
    elif len(num) < 10:
        word = toEnglishLessThanOneBillionGreaterThanOneMillion(num)
    elif len(num) < 13:
        word = toEnglishGreaterThanOneBillion(num)
    else:
        word = f"{int(num):<_d} is too large, i dont know the english word after billion!"
    return print(f"input:{int(num):<_d}, output: {word}\n\n")


def createYourOwnExample():
    while not (num := input("enter an positive integer:").strip()).isdigit():
        print("error! must be positive int")
    numToEnglish(num)


def createRandomExample():
    num = random.randint(0, (1_000_000_000_000 - 1))
    numToEnglish(str(num))


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
            '1': lambda: numToEnglish("123"),
            '2': lambda: numToEnglish("12345"),
            '3': lambda: numToEnglish("1234567"),
            '4': lambda: numToEnglish("1234567891"),
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
            print("error! must be positive int")
        func(choice)


main()
