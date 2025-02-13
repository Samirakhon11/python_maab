def are_sets_disjoint(set1, set2):
    return set1.isdisjoint(set2)     #Returns True if sets have no common elements

n1 = int(input("Enter the number of elements in the first set: "))
set1 = {input(f"Enter element {i + 1}: ") for i in range(n1)}

n2 = int(input("Enter the number of elements in the second set: "))
set2 = {input(f"Enter element {i + 1}: ") for i in range(n2)}

if are_sets_disjoint(set1, set2):
    print("The sets have no elements in common.")
else:
    print("The sets have common elements.")