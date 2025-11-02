#create a prgrm to find sum of 3 from the user
#if user doesnt provide any no ,use default as 100 200 300

num1= int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))

def sum_of_3_nos(num1=100, num2=200, num3=300):
    return num1 + num2 + num3

result = sum_of_3_nos(num1, num2, num3)
print(result)

result1 = sum_of_3_nos()
print(result1)
result2=sum_of_3_nos(num1=10)
print(result2)
result3=sum_of_3_nos(num2=10,num3=20)
print(result3)
result4=sum_of_3_nos(num1=20,num2=20,num3=20)
print(result4)

