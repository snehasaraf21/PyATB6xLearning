square = [1,2,3,4,5,6]
print(square)

print(square.pop(2))# removes the no in index 2 and also returns the value
print(square.pop())#if no index is mentioned then its removes the last value and returns it
print(square)

square.clear()#clears the full list
print(square)#prints the empty list with []

numbers = [10,20,30,20,50,60]
print(numbers.index(20))#prints index of value 30 thats 0,1,3 thats 3
print(numbers.index(50))

print(numbers.count(20))#counts the occurence of a particular value

numbers.sort()#sorts in ascending order
print(numbers)

numbers.sort(reverse=True)
print(numbers)
#sorts in descending order

numbers.reverse()#reverse of the list
print(numbers)

#max(),min(),sum() works for numerical list
print(max(numbers))#60
print(min(numbers))#10
print(sum(numbers))#190

#SLICING
print(numbers)
print(numbers[1:4])#prints from index 1 to index 4 #20 20 30
print(numbers[-1])#60#prints the last element

#in element is used to check if a element is present in alist or not it returns true or false

print("Sneha" in numbers)#false
print(20 in numbers)#true

#list and comprehension
l = list(range(1,5))
print(l)

#multiple list in one list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[0][2])

del matrix[0]#deletes a particular list from the given index
print(matrix)