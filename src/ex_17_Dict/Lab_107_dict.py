info1 = {
    "name" : "Sneha",
    "age" : 32,
    "age" : 37 ,
    "height" : 152,
    "address" :"UK"


}

info2 = {
    "name" : "Amit",
    "age" : 41,
    "height" : 152,
    "address" :"UK"

}


print(info1)#latest value will be printed in case of same key
print(info1["name"])
print(info1["age"])
print(info1["height"])
info1["height"] = 150
print(info1)

new_info = (info1, info2)#2 dic can be printed as a list together
print(new_info)

print(new_info[0]["name"])# name from first dic
print(new_info[1]["age"])#agr from second list
print(new_info[1]["height"])