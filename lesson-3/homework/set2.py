def intersection_sets(set1, set2):
    return set1 & set2              #intersection -> &

n1 = int(input("Enter the number of elements in the first set: "))
set1 = set(input(f"Enter element {i + 1}: ") for i in range(n1))

n2 = int(input("Enter the number of elements in the second set: "))
set2 = set(input(f"Enter element {i + 1}: ") for i in range(n2))

result = intersection_sets(set1, set2)

print("Intersection of both sets:", result)