my_list = [1,2,3]
my_list[0]= "Sneha"
my_list[1]= "saraf"

for item in my_list:
    print(item)

    #range is a function that returns

for i in range(1,5):#returns list 1 2 3 4
    print(i)

my_list = [1,2,3,4]# indexing always start at 0
print("element at index:",my_list[0])
print("element at index:",my_list[1])
print("element at index:",my_list[2])

#append() - append object to the end of the list
my_list.append(2)#adds 1 element at the end
print(my_list)
my_list.append(5)
print(my_list)

#extend() - extends the list
my_list.extend([6,7])
print(my_list)

my_list.extend([8,9])
print(my_list)

#insert()-- inserts in the given index
my_list.insert(2,"Sneha")#inserts in 3rd position index 0,1,2 index and restb all shifts
print(my_list)

my_list.insert(3,99)
print(my_list)
print(len(my_list))

#we can change the index value as well
my_list[1] = "Amit"#changed value in index 1 TO "Amit"
print(my_list)

#remove()--can be used to remove
my_list.remove(99)#removed 99 from the list and index shifted accordingly
print(my_list)
print(len(my_list))

#copy()--can be used to copy a list
my_copy_list = my_list.copy()
print(my_copy_list)

my_copy_list.remove("Sneha")
print(my_copy_list)#removed from copy list
print(my_list)

