def is_set_empty(my_set):
    return len(my_set) == 0 

n = int(input("Enter the number of elements in the set: "))
my_set = set(input(f"Enter element {i + 1}: ") for i in range(n))

if is_set_empty(my_set):
    print("The set is empty.")
else:
    print("The set has elements.")
