def rotate_list(my_list, num):
    num = num % len(my_list)
    return my_list[-num:] + my_list[:-num]

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)

num = int(input("Enter a number: "))
print(rotate_list(my_list, num))