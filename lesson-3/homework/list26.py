def find_middle(lst):
    n = len(lst)
    mid = n // 2  
    if n % 2 == 1:
        return lst[mid]
    else:
        return [lst[mid - 1], lst[mid]]  
    
n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)
    
result = find_middle(my_list)

print(f"The middle element is: {result}")