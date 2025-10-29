num = int(input("Enter the number to find the factorial: "))
factorial = 1
if num == 0:
    print("Factorial is", factorial)
elif num < 0:
    print("Please enter a positive number")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
        print("The factorial of", num, "is", factorial)