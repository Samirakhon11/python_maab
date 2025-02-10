def contains_digits(word):
    return any(char.isdigit() for char in word)

word = input("Enter a string: ")

if contains_digits(word):
    print("The string contains a number")
else:
    print("The string doesn't contains a number")