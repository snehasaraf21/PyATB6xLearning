#write a python prgm to calculate the area of the circle given its radius using the formula
#area = π*r^2(π = 3.14)
#i/p --> r --> float(always ask which data type)
#o/p -->string formatted o/p of area

#logic building formula
#||step 1||
#find the i/p and o/p
#i/p --> r --> data type --> float
#pi=3.14
#power --> pow or ** 2#o/p --> str  --> float - area , print area

#||step 2 ||
#rough logic = 3.14 * pow(r,2) or 3.14 * r ** 2

#||step3||
import math
radius = float(input("enter the radius of the circle"))
area= math.pi *  radius ** 2 # area =3.14987654 * (pow(radius , 2))#import math and use math.pi function
print(f"The area of the circle is: {area : .2f}")#formatting to 2 decimal points # string data formatting