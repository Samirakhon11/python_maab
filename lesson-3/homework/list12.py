n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    my_list.append(element)

while True:
    index = int(input("Enter the index of position to insert: "))
    if 0 < index <= len(my_list):
        break
    print(f"Invalid input! Please, enter a number between 0 and {len(my_list)}: ") 

new_element = input("Enter an element to insert: ")
my_list.insert(index, new_element)

print("The updated list: ", my_list)