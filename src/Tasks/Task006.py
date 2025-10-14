#write a prgm to check if a no entered by the user is greater than 100

x= float(input("enter the number"))

print(f"{x} is equal to 100" if x == 100 else f"{x} is greater than 100" if x > 100 else f"{x} is less than 100")