n = int(input("Enter the number of elements: "))
my_list = []
odd_count = 0

for i in range(n):
    element = int(input(f"Enter the element {i + 1}: ")) 
    my_list.append(element)

for i in my_list:
    if i % 2 != 0:  
        odd_count += 1

print("Number of odd elements: ", odd_count)