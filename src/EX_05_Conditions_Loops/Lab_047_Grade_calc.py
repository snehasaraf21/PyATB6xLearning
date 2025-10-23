# Grade Calculator:
#Write a prgm to calcul0ate and display0 t0he le0tter grade
#for the f0ollo0wing numerical score(A,B,C,D,E,F)
#A : 90-100
#B : 80-89
#C : 70-79
#D : 60-69
#F : 0-59

#Logic building formula
#i/p--> int o/p--> string mentioning the grade accoprdingly
#rough logic:
#if score between 90-100 then your grade is A etc etc

score = int(input("Enter your score: "))
if score > 100  or score <= 0:
    print("please enter a valid score")
elif score >= 90 and score <= 100:
     print("your grade is A")
elif score >= 80 and score <= 89:
    print("your grade is B")
elif score >= 70 and score <= 79:
    print("your grade is C")
elif score >= 60 and score <= 69:
    print("your grade is D")
else:
    print("your grade is F")