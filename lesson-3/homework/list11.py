n = int(input("Enter the number of elements: "))
original_l = []
    
for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    original_l.append(element)

final_l = list(set(original_l))

print("The new list: ", final_l)