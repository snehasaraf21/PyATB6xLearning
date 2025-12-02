
try:
    a = int(input("enter number 1:"))
    b = int(input("enter number 2:"))
    c= a/b
except TypeError:
    print("Type Error")
except ZeroDivisionError:
    print("Division by Zero")
except ValueError:
    print("Value Error")
else:
    print("c=",c)
finally:
    print("I will execute the code!!!")