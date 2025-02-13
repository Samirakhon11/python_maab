def remove_element_at_index(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    return lst

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)

to_remove = int(input("Enter index of an element to remove: "))
result = remove_element_at_index(my_list, to_remove)

print("Updated list: ", result)