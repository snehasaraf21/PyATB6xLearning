from collections import *
#where 8 is all modules from package collections

user_input = input("Enter the string: ")
count_char =Counter(user_input)
print(count_char)
print(user_input)
print(len(user_input))


#named tuple
#can be used to name the characters in tuple

#info = ("Sneha",36,True,2)
#print(info)

test = namedtuple('info',['name','age','isMarried','kids'])
t =test("Sneha",36,True,2)

print(t.name,t.age,t.isMarried,t.kids)
