#print the vowel count and consonant count in the given string and print them

input_string = "hello world!"

vowels ="aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"


vowel_count = 0
consonant_count = 0
result_vowel = list()
result_consonant = list()
for letter in input_string:
    if letter in vowels:
        vowel_count += 1
        result_vowel.append(letter)
    elif letter  in consonants:
          consonant_count += 1
          result_consonant.append(letter)

print(vowel_count)#3
print(consonant_count)
print(result_vowel)#['e', 'o', 'o']
print(result_consonant)


