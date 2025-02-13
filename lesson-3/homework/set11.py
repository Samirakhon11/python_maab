def symmetric_difference(set1, set2):
    return set1 ^ set2                # Elements in one of the sets but not both

n1 = int(input("Enter the number of elements in the first set: "))
set1 = set(input(f"Enter element {i + 1}: ") for i in range(n1))

n2 = int(input("Enter the number of elements in the second set: "))
set2 = set(input(f"Enter element {i + 1}: ") for i in range(n2))

result_set = symmetric_difference(set1, set2)

print("New set with elements in either set but not both:", result_set)