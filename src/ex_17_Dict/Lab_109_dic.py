key = ["name", "address", "age"]
value = ["Sneha", "Burgess HIll",36]

my_dict = dict(zip(key, value))
print(my_dict)

#merge 2 dict
dict1 = {"a":1, "b":2, "c":3}
dict2={"d":4,"e":5,"f":6}

merge_dict = dict1 | dict2
print(merge_dict)
print(merge_dict.get("c"))