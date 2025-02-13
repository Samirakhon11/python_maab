def union_sets(set1, set2):
    return set1 | set2      #union -> |

n1 = int(input("Enter the number of elements in the first set: "))
set1 = set(input(f"Enter element {i + 1}: ") for i in range(n1))

n2 = int(input("Enter the number of elements in the second set: "))
set2 = set(input(f"Enter element {i + 1}: ") for i in range(n2))

result = union_sets(set1, set2)

print("Union of both sets:", result)