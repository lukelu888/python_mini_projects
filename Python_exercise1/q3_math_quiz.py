# Yinglin Lu 2212059
# Xiaoan Lao 1610188
# Essem Elfakharany 2213188
# assignemnt 3 
# Sep 30, 2022


# question 3)
# use random to produce two positive one-digit integers. the program should
# then prompt the user with a question, such as:
# how much is 6(first random one-digit integer) times 7(second random one-digit integer)?
# the user then inputs the answer. the program checks the user's answer. if
# it's correct, display the message "very good" and ask another multiplication
# question. if the answer is wrong, display the message "No. try again" and
# let the user try THE SAME QUESTION repeatedly until the user gets it
# right ! a separate method should be used to generate each new question.
# this method should be called once when the app begins execution and each time
# the user answers the question correctly.


import random

def math_quiz():
    # num1=random.randint(1,9)
    # num2=random.randint(1,9)
    
    num1,num2=random.choices(range(1,10),k=2)
    
    quiz_answer=num1*num2
    user_answer=-1
    while user_answer!=quiz_answer:
       
        user_answer=input(f"how much is {num1}*{num2}?\n")
        while not user_answer.replace(".","",1).replace("-","",1).isnumeric():
            print("invalid input! try again!")
            user_answer=input(f"how much is {num1}*{num2}?\n")
        quiz_answer=str(quiz_answer)
        if user_answer==quiz_answer:
            print("Very good!")
        else:
            print("Wrong! try again!")
            
def main():
    ans="y"
    while ans=="y":
        math_quiz()
        ans=input(f"do you want to continue another quiz?(y/n)\n").lower().strip()
        while ans not in ("y","n"):
            ans=input(f"invalid input! try again!\ndo you want to continue another quiz?(y/n)\n").lower().strip()        

main()