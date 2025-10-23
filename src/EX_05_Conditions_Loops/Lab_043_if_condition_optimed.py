"""
Write a program to take user age and determine if they can go to club 21 being the age limit
"""

#logic building formula
#step 1
#i/p -->age in int
#o/p--> string "can go to club or cant go to clun"

#step 2 (rough logic)
# age > 21 " can go to club"
#age < 21 "cant go to club"


age=int(input("enter the age \n").strip())

if age <= 0 or age > 130:
    print("please enter a valid age")
else:
    if age >= 21:
       print("you can go to club")
    else:
       print("you can't go to club")

    #optimize the code
    #handle all the edge cases
