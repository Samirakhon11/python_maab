def find_second_largest(tpl):
    unique_elements = list(set(tpl))
    if len(unique_elements) < 2:
        return "There is not second largest element"
    
    unique_elements.sort(reverse = True)
    return unique_elements[1]

n = int(input("Enter the number of elements: "))
elements = tuple(int(input(f"Enter element {i + 1}: ")) for i in range(n))

result = find_second_largest(elements)

print("The second largest element is:", result)