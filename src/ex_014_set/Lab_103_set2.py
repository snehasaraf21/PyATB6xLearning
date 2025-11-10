#union set
a = {1,2,3,4,5,6}
b = {1,2,3,2,3,7,8}
print(a|b)#{1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))#same as a|b

print(a & b)#{1, 2, 3}
print(a.intersection(b))#same as a&b


print(a - b)#{4, 5, 6} all elents in a not in b
print(b -a)#{8, 7}all in b not in a

print(a ^ b)#{4, 5, 6, 7, 8}prints all elemts other than comman elements
