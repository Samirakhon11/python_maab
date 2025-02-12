n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    my_list.append(element)

to_find = input("Enter an element to find the first occurance:  ")
index = my_list.index(to_find)

print(f"The first occurance of {to_find} is in index {index}")