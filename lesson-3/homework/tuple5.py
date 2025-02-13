def get_first_element(tpl):
    return tpl[0] if tpl else "Tuple is empty"  

n = int(input("Enter the number of elements: "))
elements = tuple(input(f"Enter element {i + 1}: ") for i in range(n))

print("First element:", get_first_element(elements))