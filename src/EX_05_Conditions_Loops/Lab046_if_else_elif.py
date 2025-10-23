#to find maximum in 3 given nos
#logic building formula
#i/p --> int o/p--> string stating the maximum number
#rough logic
#if num1>num2 and also num1> num 3 then num1 is maximum
#if num2>num1 and also num2>num3 then num2 is maximum
#else num3 is maximum



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
   print(num1 , "is maximum")
elif num2 >= num3 and num2 >= num1:
    print(num2 , "is maximum")
else:
    print(num3 , "is maximum")

