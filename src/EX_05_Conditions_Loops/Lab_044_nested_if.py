#find if the given positive number is even or odd
#step1
#i/p-->int o/p-->string "even" or "odd"
#rough logic
#if num / 2 = 0 then even else odd

num = int(input("Enter a number: "))

if num >= 0:
    print(num, "is even" if num % 2 == 0 else "is odd")
else:
    print("The number is negative")
