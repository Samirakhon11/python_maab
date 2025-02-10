def remove_character(word, to_remove):
    return word.replace(to_remove, '')

string_o = input("Enter a string: ")
to_remove = input("Enter a character to remove: ")
string_n = remove_character(string_o, to_remove)

letters = string_o.split()
for to_remove in letters:
    print("After removing characters: ", string_n)
else:
    print("The string doesn't contain this character")