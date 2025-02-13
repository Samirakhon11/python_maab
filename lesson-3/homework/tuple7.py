n = int(input("Enter the number of elements: "))
elements = tuple(input(f"Enter element {i + 1}: ") for i in range(n))

print(f"There are {n} elements in the tuple")