def find_second_smallest(tpl):
    unique_elements = list(set(tpl))
    if len(unique_elements) < 2:
        return "There is not second smallest element"
    
    unique_elements.sort()
    return unique_elements[1]

n = int(input("Enter the number of elements: "))
elements = tuple(int(input(f"Enter element {i + 1}: ")) for i in range(n))

result = find_second_smallest(elements)

print("The second smallest element is:", result)