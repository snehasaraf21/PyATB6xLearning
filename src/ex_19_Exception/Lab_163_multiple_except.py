
try:
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    c= a/b
    print(c)
except (NameError,ZeroDivisionError,ValueError,TypeError):
    print("Error due to name,value or zero division")
