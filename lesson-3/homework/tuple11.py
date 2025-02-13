def find_indices(tpl, target):
    return [i for i, val in enumerate(tpl) if val == target]  

n = int(input("Enter the number of elements: "))
elements = tuple(input(f"Enter element {i+1}: ") for i in range(n))

target_element = input("Enter the element to find: ")
indices = find_indices(elements, target_element)

if indices:
    print(f"The element '{target_element}' is found at indices: {indices}")
else:
    print(f"The element '{target_element}' is not in the tuple.")
