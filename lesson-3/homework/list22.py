def list_even(my_list):
    return [element for element in my_list if element % 2 == 0]

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)

result = list_even(my_list)

print("The new list: ", result)