n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    my_list.append(element)

num_of_elements = len(my_list) 

print(f"There are {num_of_elements} elements in the list")