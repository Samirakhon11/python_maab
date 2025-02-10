string_o = input("Enter a string: ")
vowels = 'aeuio'

for vowel in vowels:
    string_o = string_o.replace(vowel, '*')

print("New string: ", string_o)
