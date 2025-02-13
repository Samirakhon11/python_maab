def find_second_largest(my_list):
    return sorted(my_list[-2])

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    my_list.append(element)

result = find_second_largest(my_list)

print(f"The second largest element is: {result}")