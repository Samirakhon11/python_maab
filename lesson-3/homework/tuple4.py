def element_exists(tpl, target):
    return target in tpl  

n = int(input("Enter the number of elements: "))
elements = tuple(input(f"Enter element {i + 1}: ") for i in range(n))

target_element = input("Enter the element to check: ")

if element_exists(elements, target_element):
    print(f"The element '{target_element}' is present in the tuple.")
else:
    print(f"The element '{target_element}' is not present in the tuple.")