student1 = {
    "name" : "Sneha",
    "age" : 22,
    "address" : {
        "city" : "Burgess hill",
        "county" : "West sussex"
    }
}

student2 = {
    "name" : "Amit",
    "age" : 32,
    "address" : {
        "city" : "Brighton",
        "county" : "East sussex"
    }
}

student3 = {
    "name" : "Vedant",
    "age" : 16,
    "address" : {
        "city" : "crawley",
        "county" : "mid sussex"
    }
}

student_info = [student1, student2, student3]
print(student_info)
print(student_info[0]["address"]["city"])
print(student_info[1]["address"]["city"])
print(student_info[2]["name"])
