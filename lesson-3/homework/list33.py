def find_indices(my_list, target):
    return [i for i in range(len(my_list)) if my_list[i] == target]

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)

target_element = input("Enter a target element: ")

print(find_indices(my_list, target_element))