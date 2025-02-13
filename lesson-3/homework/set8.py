def remove_element(my_set, element):
    my_set.discard(element)
    return my_set

n = int(input("Enter the number of elements in the set: "))
my_set = set(input(f"Enter element {i + 1}: ") for i in range(n))

element_to_remove = input("Enter the element to remove: ")

updated_set = remove_element(my_set, element_to_remove)

print("Updated set:", updated_set)