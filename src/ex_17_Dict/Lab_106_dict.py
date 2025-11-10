my_dict = {
    "name":"Sneha",
    "age":37,
    "height":152,
    "weight":42
}

print(my_dict)
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["height"])

my_dict["height"] = 160#its mutable
print(my_dict)

del my_dict["height"]
print(my_dict)

for key , value in my_dict.items():
    print(key , value)

print("age" in my_dict#True
print("height" in my_dict)#false as we del it
print("weight" in my_dict)#true