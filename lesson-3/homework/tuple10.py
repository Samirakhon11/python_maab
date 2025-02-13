def is_tuple_empty(tpl):
    return "Tuple is not empty" if tpl else "Tuple is empty"

n = int(input("Enter the number of elements: "))
elements = tuple(input(f"Enter element {i + 1}: ") for i in range(n))

print(is_tuple_empty(elements))