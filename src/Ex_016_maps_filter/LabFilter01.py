num = [1,2,3,4,5,6]

def even_no(x):
    return x % 2 == 0

even_no_r = list(filter(even_no,num))#filterd only the elements that are true to the function i,e num % 2 ==0
print(even_no_r)