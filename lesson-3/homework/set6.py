def count_unique_elements(my_set):
    return len(my_set)

n = int(input("Enter the number of elements in the set: "))
my_set = set(input(f"Enter element {i + 1}: ") for i in range(n))

unique_count = count_unique_elements(my_set)

print(f"The number of unique elements in the set: {unique_count}")