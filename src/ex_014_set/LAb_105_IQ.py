#prgm to find the first non repeating string in the given word
#ex "Swiss" ans is w as its the first non repeating character

def for_non_repeating_chars(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None


result=for_non_repeating_chars("swiss")
print(result)
result=for_non_repeating_chars("annusinha")
print(result)
result=for_non_repeating_chars("snehasaraf")
print(result)
