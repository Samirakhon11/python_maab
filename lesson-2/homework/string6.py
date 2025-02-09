word = input("Enter a string: ")
word_e = word.lower()
word_to_check = input("Enter a string to find: ")
word_to_check_e = word_to_check.lower()

if word_to_check_e in word_e:
    print("This word exists in the string")
else:
    print("This word doesn't exist in the string")