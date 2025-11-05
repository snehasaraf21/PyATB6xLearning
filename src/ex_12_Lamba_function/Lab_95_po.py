import math
#def pow(num):
#    return math.pow(num,2)

#result = pow(10)
#print(result)

num = int(input("Enter a number: "))
pow_l =  lambda  num : math.pow(num,2)
print(pow_l(num))

pow_l = lambda : math.pow(int(input("Enter the number:")),2)
print(pow_l())
