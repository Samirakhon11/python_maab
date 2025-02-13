def add_to_set(my_set, element):
    if element not in my_set:
        my_set.add(element)
        print(f"Element '{element}' added to the set.")
    else:
        print(f"Element '{element}' is already in the set.")

n = int(input("Enter the number of elements in the set: "))
my_set = set(input(f"Enter element {i + 1}: ") for i in range(n))

element = input("Enter the element to add: ")

add_to_set(my_set, element)

print("Updated set:", my_set)