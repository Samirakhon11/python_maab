def replace_first_occurrence(my_list, old, new):
    if old in my_list:  
        index = my_list.index(old)  
        my_list[index] = new 
    return my_list

n1 = int(input("Enter the number of elements for the first list: "))
my_list = []
    
for i in range(n1):
    element = input(f"Enter the element {i + 1}: ")
    my_list.append(element)

old_element = input("Enter an element that you want to change: ")
new_element = input("Enter a new element: ")

updated_list = replace_first_occurrence(my_list, old_element, new_element)
print(updated_list)
