def count_occurrences(tpl, target):
    return tpl.count(target)

n = int(input("Enter the number of elements: "))
elements = tuple(input(f"Enter element {i + 1}: ") for i in range((n)))

target_element = input("Enter the element to count: ")

print(f"Element {target_element} occurs {count_occurrences(elements, target_element)} times")