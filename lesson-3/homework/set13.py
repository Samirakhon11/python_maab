def remove_random_element(my_set):
    if my_set:  
        removed_element = my_set.pop() 
        print(f"Removed element: {removed_element}")
    else:
        print("The set is empty. Nothing to remove.")

n = int(input("Enter the number of elements in the set: "))
my_set = set(input(f"Enter element {i + 1}: ") for i in range(n))

remove_random_element(my_set)

print("Updated set:", my_set)