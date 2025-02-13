def check_element(my_set, element):
    if element in my_set:
        print(f"{element} exists in the set.")
    else:
        print(f"{element} does NOT exist in the set.")

n = int(input("Enter the number of elements in the set: "))
my_set = set(input(f"Enter element {i + 1}: ") for i in range(n))

element = input("Enter the element to check: ")

check_element(my_set, element)
