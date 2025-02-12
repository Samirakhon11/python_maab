n = int(input("Enter the number of elements:  "))
original_l = []
    
for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    original_l.append(element)

final_l = original_l[::-1]

print("The new list: ", final_l)