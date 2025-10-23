#find max between 2 nos
#logic building
#i/p --> number(int or float as per requirement) o/p-->num 1 is max or num2 is max
#rough logic
#if num >= num2 then num1 is max
#or num 2 is max

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(num1 , "is maximum")
else:
    print(num2 , "is maximum")