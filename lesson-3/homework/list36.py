def sum_positive(lst):
    return sum(num for num in lst if num > 0)

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)

print(sum_positive(my_list))