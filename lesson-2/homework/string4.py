def isPalindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

input_string = input("Enter a string: ")
if isPalindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')