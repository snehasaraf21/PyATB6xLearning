a = int(input("enter number 1:"))
b = int(input("enter number 2:"))
try:
    c= a/b
    print(c)
except ZeroDivisionError:
    print("Error because division by zero")

