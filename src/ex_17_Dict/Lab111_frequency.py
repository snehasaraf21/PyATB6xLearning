#prgm to find the frequency of the character in the given string
#ex automation -->  frequency of a is 2 as its occuring 2 times

#logic building  formula
#i/p--> string o/p-->dict {} with frequency of each chracter in dict(key:value) pair


string = input("Enter a string:\n ")

char_count ={}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)