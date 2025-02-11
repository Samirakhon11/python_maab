n = int(input("Enter the number of elements in the list: "))
elements = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    elements.append(element)

to_count = input("Enter an element to count: ")
count = elements.count(to_count)

print(f"The element {to_count} appears {count} times")