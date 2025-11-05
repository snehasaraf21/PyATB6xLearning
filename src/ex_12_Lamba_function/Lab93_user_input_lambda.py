    #take a user input to find even/odd

user_input = int(input("Enter a number: "))

check_even_odd = lambda num : "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(user_input))