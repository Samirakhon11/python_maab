n = int(input("Enter the number of elements (n >= 3): "))
original_l = []

while n < 3:
    n = int(input("Enter a number bigger than 3: "))
    
for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    original_l.append(element)

final_l = original_l[:3]

print("The new list:  ", final_l)