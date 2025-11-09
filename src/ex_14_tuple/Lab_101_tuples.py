cities = ("London","Paris","New york","Rome")
print(len(cities))#4
print("Paris" in cities)#true
print("mumbai" in cities)#false


t = (9,12,34,2)
#print(t.append(12))#AttributeError: 'tuple' object has no attribute 'append'
#as tuples are unmutable ,cannot be motified


colors = ("red","blue","green")# for loop can be used to find the contents of tuple , we dont have to convert it to list
for c in colors:
    print(c)

numbers = (1,2) * 3# prints tuple *3 times
print(numbers)#(1, 2, 1, 2, 1, 2)

numbers2= ("Sneha\n") * 3
print(numbers2)


nums = (1,2,3,4,4,3)
print(len(nums))#6
print(nums.count(3))#2
print(nums.index(4))#3

my_list = (1,2,3,4,4,3)
my_tuple = tuple(my_list)
print(my_tuple)

back_to_list= list(my_tuple)
print(back_to_list)
print(max(my_tuple))
print(min(my_tuple))
print(sum(my_tuple))

my_list = (1,2,3)
print(my_list  [0:2])#it prints index 0,1# 1,2
print(my_list[-1])#last element #3
