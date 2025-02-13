def big_list(my_list, size):
    return [my_list[i:i + size] for i in range(0, len(my_list), size)]

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)

size = int(input("Enter a number: "))
print(big_list(size))