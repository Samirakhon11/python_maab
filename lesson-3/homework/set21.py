def remove_duplicates(lst):
    return list(set(lst))  

n = int(input("Enter the number of elements: "))
lst = [input(f"Enter element {i + 1}: ") for i in range(n)]

unique_list = remove_duplicates(lst)

print("List after removing duplicates:", unique_list)