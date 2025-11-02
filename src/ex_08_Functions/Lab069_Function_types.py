#built in function


result = max(3,4)
print(result)

#user defined
#no return no parameter
def greet():
    print("Hello")


#no return with parameter/arguments
def greet(name):
    print("Hello",name)

greet("Sneha")

#no return but with default parameter
def say_hello_name(name="Sneha"):
    print("Hello",name.upper())

say_hello_name()
say_hello_name("Saraf")

#multiple arguments
def multi_arge(name1="A", name2="B"):
    print("Mul--->", name1, name2)


multi_arge()#no parameter
multi_arge(name1="Sneha", name2="Saraf")#multi
multi_arge(name1="Sneha")#only 1 parameter
multi_arge(name2="Saraf")#any parameter
multi_arge(name2="Sneha", name1="Saraf")#interchange of parameter

#parameter with return
def sum_of_two(a,b):
    return a+b

result = sum_of_two(3,4)
print(result)

def sum_of_two_with_default (num1=100,num2=200)
    print("sum of two nos:")
    return num1+num2


result = sum_of_two_with_default(num1=10,num2=30)
print(result)
result = sum_of_two_with_default ()
print(result)



