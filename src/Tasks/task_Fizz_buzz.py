"""num = int(input("Enter the number:"))
if num % 3==0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3==0:
    print("Fizz")
else:
    print("Buzz")"""

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)