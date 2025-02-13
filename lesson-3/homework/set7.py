def list_to_unique_set(my_list):
    return set(my_list)

n = int(input("Enter the number of elements in the list: "))
my_list = [input(f"Enter element {i + 1}: ") for i in range(n)]

unique_set = list_to_unique_set(my_list)

print("The new set with unique elements:", unique_set)