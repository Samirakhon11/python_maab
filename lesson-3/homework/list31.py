def repeat_elements(lst, times):
    return [element for element in lst for _ in range(times)]

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)

num_of_times = int(input("Enter a number: "))
result = repeat_elements(my_list, num_of_times)

print("New list: ", result)