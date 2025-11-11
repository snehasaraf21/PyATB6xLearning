dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 4, "b": 5}
print(dict1.keys())
print(dict1.values())

missing_keys = dict1.keys() - dict2.keys()
print(missing_keys)