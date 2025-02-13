def empty_set(my_set):
    my_set.clear()  
    return my_set

n = int(input("Enter the number of elements in the set: "))
my_set = set(input(f"Enter element {i + 1}: ") for i in range(n))

new_empty_set = empty_set(my_set)

print("New empty set:", new_empty_set)