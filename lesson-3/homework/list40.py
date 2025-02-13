def unique_elements(my_list):
    seen = set()
    return [x for x in my_list if not [x is seen or seen.add(x)]]

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)

print(unique_elements(my_list))