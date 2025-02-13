n = int(input("Enter the number of elements: "))
my_list = [input(f"Enter element {i + 1}: ") for i in range(n)]

my_tuple = tuple(my_list)

print("The tuple is:", my_tuple)
