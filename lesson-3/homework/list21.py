def find_second_smallest(my_list):
    return sorted(my_list[1])

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    my_list.append(element)

result = find_second_smallest(my_list)

print(f"The second smallest element is: {result}")