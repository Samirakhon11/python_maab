def sorted_ascending(lst):
    return lst == sorted(lst)

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)

print(f"Sorted list: {sorted_ascending(my_list)}")