n1 = int(input("Enter the number of elements for the first list: "))
my_list1 = []
    
for i in range(n1):
    element = input(f"Enter the element {i + 1}: ")
    my_list1.append(element)

n2 = int(input("Enter the number of elements for the second list: "))
my_list2 = []
    
for i in range(n2):
    element = input(f"Enter the element {i + 1}: ")
    my_list2.append(element)

final_list = my_list1 + my_list2

print("Combined list: ", final_list)