# Yinglin Lu 2212059
# Oct 06, 2022

import numpy as np


a=np.asarray([1,2])
print(a)


import random
from statistics import mean


class NumList:
    def __init__(self,randomList):
        self.randomList = randomList
        
    def print_numbers(self):
        if self.randomList:
            print("Here is the list:\n[ "+" ".join(map(str,self.randomList))+" ]\n\n")
            
            #another way to print: cast to string and replace the , with space
            # print("Here is the list:\n"+str(self.randomList).replace(","," ")+"\n\n")
        else:
            print("[]- the list is empty\n\n")

    def add_number_duplicate_allowed(self):
        while True:
            added_number = input("enter an integer:").strip()
            if added_number.replace("-","",1).isdigit():
                self.randomList.append(int(added_number))
                print(f"{added_number} sucessfully added!\n\n")
                break
            else:
                print("Invalid input! Try again!")
                
    def add_number_duplicate_forbidden(self):
        while True:
            added_number = input("enter an integer:").strip()
            if added_number.replace("-","",1).isdigit():
                if int(added_number) in self.randomList:
                    print(f"{added_number} already exist in the list, try agian!")
                else:    
                    self.randomList.append(int(added_number))
                    print(f"{added_number} sucessfully added!\n\n")
                    break
            else:
                print("Invalid input! Try again!")       
        
        
        
    def display_mean(self):
        if self.randomList:
            print(f"the average of the random list {self.randomList} is {mean(self.randomList):.2f}\n\n")
        else:
            print("Unable to calculate the mean - no data!\n\n")
            
            
    def display_smallest_number(self):
        if self.randomList:
            print(f"the smallest number of the random list {self.randomList} is {min(self.randomList)}\n\n")
        else:
            print("Unable to determine smallest number - no data!\n\n")

    def display_largest_number(self):
        if self.randomList:
            print(f"the largest number of the random list {self.randomList} is {max(self.randomList)}\n\n")
        else:
            print("Unable to determine largest number - no data!\n\n")

    def clear_list(self):
        self.randomList.clear()
        print("the list is totally cleared!\n\n")
        
    def find_number(self):
        while True:
            num= input("enter the integer you want to find:").strip()
            if num.replace("-","",1).isdigit():
                num=int(num)
                break
            else:
                print("invalid input! try again!")
        if num in self.randomList:
            print(f"{num} is in the list and appreared {self.randomList.count(num)} times\n\n")
        else:
            print(f"{num} is not in the list\n\n")
    
    
    def remove_duplicates(self):
        
        #use set to remove duplicate, the list order may change
        self.randomList=list(set(self.randomList))
        
        #enumerate list comprehension to remove duplicate if dont want the list order be changed
        # self.randomList=[value for i, value in enumerate(self.randomList) if value not in self.randomList[:i]] 
        
        print(f"the duplicate entries are removed , the new list is {self.randomList}\n\n")
    
    
    
    def remove_number_with_specific_index(self):
        if self.randomList:
            while True:
                index=input("enter the index of the number that you want to remove:").strip()
                if index.replace("-","",1).isdigit() and -len(self.randomList)<=int(index)<len(self.randomList):
                    value=self.randomList[int(index)]
                    self.randomList.pop(int(index))
                    print(f"the value {value} at index {index} is removed, the new list is {self.randomList}\n\n")
                    break
                else:
                    print("invalid input for index! try again!") 
        else:
            print("[]-empty list, cannot remove a number!\n\n")
    
    
    
    def remove_number_with_all_intances(self):
        if self.randomList:
            while True:
                num=input("enter the value of the number that you want to remove:").strip()
                if num.replace("-","",1).isdigit():
                    if int(num) in self.randomList:
                        # [self.randomList.remove(int(num)) for _ in range(self.randomList.count(int(num)))]
                        self.randomList= list(filter(lambda x:x!=int(num), self.randomList))
                        
                        
                        print(f"all instances of the number {num} are removed, the new list is {self.randomList}\n\n")
                        break
                    else:
                        print(f"{num} is not in the list.")
                else:
                    print("invalid input! the number must be integer! try again!") 
        else:
            print("[]-empty list, cannot remove a number!\n\n")
    
    
    
    def reverse_sort(self):
        self.randomList.sort(reverse=True)
        print(f"the new list after descending sort is {self.randomList}\n\n")
    
    
    
    def quit_program(self):
        print("Thank you for using! GoodBye!\n\n")





def func(i,numList):
    case=  {
            "P" : numList.print_numbers,
            "A" : numList.add_number_duplicate_allowed,
            "B" : numList.add_number_duplicate_forbidden,
            "M" : numList.display_mean,
            "S" : numList.display_smallest_number,
            "L" : numList.display_largest_number,
            "C" : numList.clear_list,
            "F" : numList.find_number,
            "D" : numList.remove_duplicates,
            "I" : numList.remove_number_with_specific_index,
            "R" : numList.remove_number_with_all_intances,
            "Y" : numList.reverse_sort,
            "Q" : numList.quit_program 
            }
            
    fun=case.get(i,lambda: print("Unknown selection, please try again!\n\n"))
    return fun()



def menu():
    print(      "Select an option: \n" 
                "P - Print numbers \n" 
                "A - Add a number (allowing duplicate entries) \n" 
                "B - Add a number (not allowing duplicate entries) \n" 
                "M - Display mean of the numbers \n" 
                "S - Display the smallest number \n" 
                "L - Display the largest number \n" 
                "C - Clearing out the list \n" 
                "F - Find a number and display times in occurance \n" 
                "D - Remove duplicates (This is my own Functionality) \n" 
                "I - Remove an entry at an index in the list (This is my own Functionality) \n" 
                "R - Remove all instances of a number from the list (This is my own Functionality) \n" 
                "Y - Sort the list in descending order (This is my own Functionality) \n" 
                "Q - Quit \n")


def main():

    numList=NumList(random.sample(range(100),10))
    choice='0'
    while choice!='Q':
        menu()
        choice=input("Enter your choice:").strip().upper()
        func(choice,numList)

        
main()