name = ["Sneha","Amit","Vedant","Ritvi"]

def upper_case(string):
    return string.upper()

upper = list(map(upper_case,name))#applies function to every element in list
print(upper)