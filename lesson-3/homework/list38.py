def is_palindrome(lst):
    return lst == lst[::-1]

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)

print(is_palindrome(my_list))