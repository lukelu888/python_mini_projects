# Yinglin Lu 2212059
# Xiaoan Lao 1610188
# Essem Elfakharany 2213188
# assignemnt 3 
# Sep 30, 2022

# Question 2)
# Imagine a relation between 2 numbers in such :
# the sum of factors including 1 (but not the number itself) of one number
# is equal to the other number and vice versa.
# for example, (220,284) have such a relation. the factors of 220 are
# 1,2,4,5,10,11,20,22,44,55, and 110 whose sum equals 284. the factors of 284
# are 1,2,4,71,142 whose sum equals 220.
# Write a function checkRelation which you call from main() and checks
# whether a pair of numbers entered has this relation or has not. Display
# the factors of each number to confirm your answer.

import random

def get_factors(n):
    # factors=[]
    # for i in range(1,int(n/2)+1):
    #     if n%i==0:
    #         factors.append(i)
    # return factors     
    return [i for i in range(1,int(n/2)+1) if n%i==0]  


def check_relation(num1,num2):
    sum1,sum2=0,0
    if num1<=1 or num2<=1:
        print(f"the input {num1},{num2} is invalid for checking amicable numbers relation!")
    else:
        factors1=get_factors(num1)
        factors2=get_factors(num2)
        sum1=sum(factors1)
        sum2=sum(factors2)
        print(f"the factors of {num1} is {factors1}, the sum is {sum1}")
        print(f"the factors of {num2} is {factors2}, the sum is {sum2}")
        if sum1==num2 and sum2==num1:
            print(f"{num1} and {num2} has an amicable number relation!")
        else:
            print(f"{num1} and {num2} dont have an amicable number relation!")


def main():
    
    print("1.Generate two random numbers and check relation:")
    num1=random.randint(1,1000)
    num2=random.randint(1,1000)
    print(f"we generate two random numbers ({num1}, {num2})")
    check_relation(num1, num2)
    
    print("2.get user input for check relation:")
    
    while True:
        try:
            num1,num2=input("enter two positive ints split by space:").split()
            num1=int(num1)
            num2=int(num2)
            break
        except Exception as e:
            print(e)
    
    # while True:
    #     num1=input("enter first positive integer:").strip()
    #     if num1.isdigit() and int(num1)>0:
    #         num1=int(num1)
    #         break
    #     else:
    #         print("invalid input!Try again")
        
    # while True:
    #     num2=input("enter second positive integer:").strip()
    #     if num2.isdigit() and int(num2)>0:
    #         num2=int(num2)
    #         break
    #     else:
    #         print("invalid input!Try again")
            
    check_relation(num1, num2)


    
main()