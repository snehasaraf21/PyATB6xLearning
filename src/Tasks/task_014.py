#Create a function which will take a positive number from the user and perform square of the number?
#i/o = 3
#o/p = 9

"""def power_of_number(a):
    return pow(a,2)

power_result=power_of_number(3)
print(power_result)"""


def power_of_number():
    global num
    num=int(input("Enter a number: "))
    return pow(num,2)


power_result=power_of_number()
print(f"power of {num} is {power_result}")
