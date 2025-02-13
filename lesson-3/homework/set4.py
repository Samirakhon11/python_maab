def check_subset(set1, set2):
    if set1.issubset(set2):
        print("The first set is a subset of the second one")
    elif set2.issubset(set1):
        print("The second set is a subset of the first one")
    else:
        print("Neither set is a subset of the other.")

n1 = int(input("Enter the number of elements in the first set: "))
set1 = set(input(f"Enter element {i + 1}: ") for i in range(n1))

n2 = int(input("Enter the number of elements in the second set: "))
set2 = set(input(f"Enter element {i + 1}: ") for i in range(n2))

check_subset(set1, set2)