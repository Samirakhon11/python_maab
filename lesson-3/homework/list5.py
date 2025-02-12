def check_in_list(element, my_list):
    if element in my_list:
        return f"The element {element} exists in the list"
    else:
        return f"The element {element} doesn't exist in the list"

n = int(input("Enter the number of elements: "))
elements = []

for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    elements.append(element)

to_find = input("Enter an element to find: ")
result = check_in_list(to_find, elements)

print(result)