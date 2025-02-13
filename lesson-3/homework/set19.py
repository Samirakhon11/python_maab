def merge_lists_to_set(list1, list2):
    return set(list1 + list2)  

n1 = int(input("Enter the number of elements in the first list: "))
list1 = [input(f"Enter element {i + 1}: ") for i in range(n1)]

n2 = int(input("Enter the number of elements in the second list: "))
list2 = [input(f"Enter element {i + 1}: ") for i in range(n2)]

merged_set = merge_lists_to_set(list1, list2)

print("Merged set:", merged_set)