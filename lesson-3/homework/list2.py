n = int(input("Enter the number of elements: "))
elements = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    elements.append(element)

total = 0

for i in range(n):
    total += elements[i] 

print(total)