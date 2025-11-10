names = ["QA","","Sneha","","Amit"]

def empty_name(x):
    return x != ""

result = list(filter(empty_name,names))
print(result)