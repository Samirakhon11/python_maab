n = int(input("Enter the number of elements: "))
my_list = []
even_count = 0

for i in range(n):
    element = int(input(f"Enter the element {i + 1}: ")) 
    my_list.append(element)

for i in my_list:
    if i % 2 == 0:  
        even_count += 1
        

print("Number of even elements: ", even_count) 