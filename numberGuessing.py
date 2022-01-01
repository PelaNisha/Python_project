# number guessing
import random

found = False
def sel_rad():
    return random.randint(1,10) 
       
x = sel_rad()
while(found==False):
    a = int(input("Enter your guess: "))
    if(a!=x):
        if(a>x):
            print("Lesser")
        else:
            print("Greater")  
    else:
        print("Right!!")
        found = True          