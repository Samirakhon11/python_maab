n = int(input("Enter the number of elements: "))
original_l = []
    
for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    original_l.append(element)

original_l.sort()

print("The new list:  ", original_l)