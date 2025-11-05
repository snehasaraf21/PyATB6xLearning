
#Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
"""def type_of_triangle(side1,side2,side3):
    if side1==side2==side3:
        print("Its a equilateral triangle")
    elif side1==side2 or side2==side3 or side3==side1:
        print("Its a isosceles triangle")
    else:
        print("Its a scalene triangle")

type_of_triangle(side1=2,side2=2,side3=2)
type_of_triangle(side1=3,side2=2,side3=2)
type_of_triangle(side1=4,side2=2,side3=3)"""


def type_of_triangle():
    side1 = float(input("Enter the side 1 of the triangle: "))
    side2 = float(input("Enter the side 2 of the triangle: "))
    side3 = float(input("Enter the side 3 of the triangle: "))
    if side1>0 and side2 > 0 and side3 > 0:
        if side1+side2 > side3 and side1+side3 > side2 and side2+side3 > side1:
           if side1 == side2 == side3:
              print("Its a equilateral triangle")
           elif side1 == side2 or side2 == side3 or side3 == side1:
              print("Its a isosceles triangle")
           else:
              print("It s a scalene triangle")
        else:
            print("its not  triangle")
    else:
        print("invalid lenght of the triangle")



type_of_triangle()



