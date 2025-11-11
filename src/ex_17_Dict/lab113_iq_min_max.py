#function that returns max value in the dic
#{"a":10 , "b":20,"c":30}
#o/p is 30 for value and c for key

def max_value(dict):
    return max(dict.values())

print(max_value({"a":10 , "b":20,"c":30}))#30

def min_value(dict):
    return min(dict.values())
print(min_value({"a":10 , "b":20,"c":30}))#10

def max_key(dict):
    return max(dict.keys())

print(max_key({"a":10 , "b":20,"c":30}))#c


def min_key(dict):
    return min(dict.keys())
print(min_key({"a":10 , "b":20,"c":30}))#a