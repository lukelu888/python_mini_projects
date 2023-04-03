# Yinglin Lu 2212059
# assignemnt 3 
# Sep 30, 2022


# Question 1)
# You are working on a project and need to cut films into scenes. to help streamline the creation of the final films, the team needs to
# develop an automated way of breaking up individual shots (short sequence from a particular camera angle) in a film into scenes
# (a sequence of shots). there is already an algorithm that breaks the film up into shots and                                                                                                                                                                                                                 labels them with a letter. Identical shots are labelled with the same letter. write a function to split the film into as many short scenes as
# possible without confusing viewers by having the same shot appear in different scenes. This will partition the sequence of shot labels into
# scenes so that no shot label appears in more than one scene and each scene is as short as possible. the output should
# be the length of each scene.
# Input
# the input to the function/method consists of a list of characters representing the sequence of shots.
# Output
# Return a list of integers representing the length of each scene, in the order in which it appears in the given sequence of shots.
# example 1:
# inputList = ['a','b','a','b','c','b','a','c','a','d','e','f','e','g','d','e','h','i','j','h','k','l','i','j']
# output: [9,7,8]
# example 2:
# inputList=[a,b,c]
# output:[1,1,1]
# example 3:
# inputList =[a,b,c,a]
# output: [4]
# Example 4:
# inputList = [a,b,c,d,a,e,f,g,h,i,j,e]
# output:[5 7]
# Example 5:
# inputList = ['z', 'w', 'c', 'b', 'z', 'c', 'h', 'f', 'i', 'h', 'i']
# output: [6, 5]


import random
import string


def split_scene(film):
    size,end=0,0
    res=[]
    input="".join(map(str,film))
    for i, c in enumerate(input):
        size+=1
        last_index=input.rindex(c)
        # last_index = max(i for i, char in enumerate(film) if char == c) # if input is a list not str, use this way
        end=max(end,last_index)
        if i==end:
            res.append(size)
            size=0
            
    print("\nInputList = ", film)
    print("Output:", res,"\n")


def create_list(i):
    case={
        '1': ['a', 'b', 'a', 'b', 'c', 'b', 'a', 'c', 'a', 'd', 'e', 'f', 'e', 'g', 'd', 'e', 'h', 'i', 'j', 'h', 'k', 'l', 'i', 'j'],
        '2': ['a', 'b', 'c'],
        '3': ['a', 'b', 'c', 'a'],
        '4': ['a', 'b', 'c', 'd', 'a', 'e', 'f', 'g', 'h', 'i', 'j', 'e'],
        '5': ['z', 'w', 'c', 'b', 'z', 'c', 'h', 'f', 'i', 'h', 'I']
    }
    if i=='6':
        case['6'] = input("enter a list of characters with comma to seperate: ").lower().replace(" ","").split(',')
    if i=='7':
        size=random.randint(1,20);
        # randList=[]
        # for n in range(size):
        #     randList.append(random.choice(string.ascii_lowercase))
        # case[i]=randList
        
        case[i]=random.choices(string.ascii_lowercase,k=size)
     
    generated_list = case[i]
   
    return generated_list

def menu():
    print("1.Example 1\n"
          "2.Example 2\n"
          "3.Example 3\n"
          "4.Example 4\n"
          "5.Example 5\n"
          "6.Enter you own list\n"
          "7.Create random list\n"
          "0.Exit the program\n")

def main():
  
    while 1:
        menu()
        
        # while True:
        #     choice=input("Enter your choice(0-7):").strip()
        #     if choice.isdigit() and 0<=int(choice)<=7:
        #         break
        #     else:
        #         print("invalid input! Try again!")
        
        while True:
            try:
                choice=int(input("Enter your choice(0-7):").strip())
                if 0<=choice<=7:
                    break
            except Exception:
                print("invalid input! Try again!")
                
        if choice=='0':
            print("thank you for using!")
            break    
        else:
            split_scene(create_list(choice))


        
            
main()           

