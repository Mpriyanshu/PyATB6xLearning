input_string = "hello, world!"


vowels = "aeiou"
consonants = "bcdfghjklmnpqrst"

vowels_count = 0
consonant_count = 0
result = dict()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count+1
    elif char in consonants:
        consonant_count = consonant_count+1



print(vowels_count)
print(consonant_count)