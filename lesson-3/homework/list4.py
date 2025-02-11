n = int(input("Enter the number of elements: "))
elements = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    elements.append(element)

minimum = elements[0]
for i in range(1, n):
    if elements[i] < minimum:
        minimum = elements[i]
        
print("The minimum element is: ", minimum)