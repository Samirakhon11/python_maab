def unique_tuple(tpl):
    seen = set()
    return tuple(element for element in tpl if element not in seen and not seen.add(element))

n = int(input("Enter the number of elements: "))
tpl = tuple(input(f"Enter element {i + 1}: ") for i in range(n))

result = unique_tuple(tpl)

print("Tuple with unique elements:", result)