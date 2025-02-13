def first_three_elements(tpl):
    return tpl[:3]  

n = int(input("Enter the number of elements: "))
elements = tuple(input(f"Enter element {i + 1}: ") for i in range(n))
new_tuple = first_three_elements(elements)

print("New tuple with first three elements: ", new_tuple)
