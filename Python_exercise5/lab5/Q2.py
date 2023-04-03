import random


def largestMultipleOfThree(arr):
    remainder0 = []
    remainder1 = []
    remainder2 = []

    arr.sort()
    sumArr = sum(arr)
    for i in arr:
        if i % 3 == 2:
            remainder2.append(i)
        elif i % 3 == 1:
            remainder1.append(i)
        else:
            remainder0.append(i)

    if sumArr % 3 == 1:
        if len(remainder1) > 0:
            remainder1.pop(0)
        else:
            remainder2.pop(0)
            remainder2.pop(0)

    if sumArr % 3 == 2:
        if len(remainder2) > 0:
            remainder2.pop(0)
        else:
            remainder1.pop(0)
            remainder1.pop(0)

    result = []
    result.extend(remainder0)
    result.extend(remainder1)
    result.extend(remainder2)
    result.sort(reverse=True)

    if len(result) == 0:
        return ""

    if (result[0] == 0):
        return "0"
    else:
        return "".join(map(str, result))


def createYourOwnExample():
    while not (size := input("enter the size of the list:").strip()).isdigit():
        print("error! must be positive int")
    inputList = []
    for i in range(int(size)):
        while (not (num := input("enter an positive integer:").strip()).isdigit()) or 10 < int(num) < 0:
            print("error! must be an int (0-9)")
        inputList.append(int(num))
    print(f"input:{inputList}, output: {largestMultipleOfThree(inputList)}\n\n")


def createRandomExample():
    size = random.randint(0, 10)
    inputList = []
    for i in range(size):
        inputList.append(random.randint(0, 9))
    print(f"input:{inputList}, output: {largestMultipleOfThree(inputList)}\n\n")


def menu():
    print("[0]- exit")
    print("[1]- Exemple: [8,1,9]")
    print("[2]- Exemple: [8,7,6,1,0]")
    print("[3]- Exemple: [1]")
    print("[4]- Exemple: [0,0,0,0]")
    print("[5]- Enter your own example:")
    print("[6]- create random example:")


def func(i):
    case = {'0': lambda: print("Good Bye!"),
            '1': lambda: print(f"input:{[8, 9, 1]}, output: {largestMultipleOfThree([8, 9, 1])}\n\n"),
            '2': lambda: print(f"input:{[8, 7, 6, 1, 0]}, output: {largestMultipleOfThree([8, 7, 6, 1, 0])}\n\n"),
            '3': lambda: print(f"input:{[1]}, output: {largestMultipleOfThree([1])}\n\n"),
            '4': lambda: print(f"input:{[0, 0, 0, 0]}, output: {largestMultipleOfThree([0, 0, 0, 0])}\n\n"),
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
