squares = {x ** 2 for x in range(5)}
print(squares)
#but this 1 liner method is ideally not recommended as its bit confusing

#frozenset is a set that cannot  be changed(immutable)

fset = frozenset([1,2,3])
print(fset)
print(fset.add(10))#ttributeError: 'frozenset' object has no attribute 'add'



