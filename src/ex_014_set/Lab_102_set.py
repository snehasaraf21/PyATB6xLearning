#set is a collection of unique elementsi,e duplicates are gone
#{} paranthesis or curly braces are used

list_of_unique_elements = {1,2,3,2,3,2,4,5,6}
print(list_of_unique_elements)#{1, 2, 3, 4, 5, 6}#repeated elemnts are gone

list_of_unique_elements2 = {"Sneha",1,3.14,1,2,1,2}#mixed data types
print(list_of_unique_elements2)

list1 = [1,2,3,3,4,2]
set1= set(list1)#{1, 2, 3, 4}
# repeatation 3 is gone
print(set1)


list2= ("Sneha","Ritvi","Vedant","Amit","Sneha")#{'Vedant', 'Amit', 'Ritvi', 'Sneha'}
set2= set(list2)
print(set2)

#empty set
empty = set()
print(type(empty))

for items in list2:
    print(items)


list1.append(4)
print(list1)

list_of_unique_elements2.add(10)#adds 10 to the set
print(list_of_unique_elements2)

list_of_unique_elements2.remove(10)
print(list_of_unique_elements2)#removes 10