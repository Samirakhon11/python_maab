def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

n1 = int(input("Enter the number of elements: "))
my_list1 = []
    
for i in range(n1):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list1.append(element)

n2 = int(input("Enter the number of elements: "))
my_list2 = []
    
for i in range(n2):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list2.append(element)

print("New list: ", merge_sorted_lists(my_list1, my_list2))