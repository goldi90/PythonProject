import random
num=random.randint(1,50)
Unum= int(input("Enter Your the number: "))
n=10
for i in range(0,n+1): # this line runs loop 10 Times
    if num!=Unum: # if the given number is not equal to random number 
        Unum=int(input("Try Again Guess the number: ")) # ask for input again
        print("You tried "+str(i+2)+" time") #this line show show how amny time user tryed 
        if i==5: # if loop completed half  ask user do you want to try again
            print("if you want to try agin pls press Y Key either N ")
            UserDecision=input("Do You Want To ty Again")
            if UserDecision=="Y" or UserDecision=="y":  # if user enter smal or caplital y it will ask another 5 time 
                pass 
            else:    
                break # if user intred any this else  than y it close program
        if i==10: # if all chance is over 
            print("you Lost Number is:"+str(num))
if num==Unum: 
        print("You Got it")