def is_palindrome(tpl):
    return tpl == tpl[::-1]  

n = int(input("Enter the number of elements: "))
tpl = tuple(input(f"Enter element {i + 1}: ") for i in range(n))

if is_palindrome(tpl):
    print("The tuple is a palindrome.")
else:
    print("The tuple is NOT a palindrome.")