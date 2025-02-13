def create_subtuples(tpl, size):
    subtuples = tuple(tpl[i:i + size] for i in range(0, len(tpl), size))

n = int(input("Enter the number of elements: "))
tpl = tuple(int(input(f"Enter element {i + 1}: ")) for i in range(n))

size = int(input("Enter the size of each subtuple: "))
new_tuple = create_subtuples(tpl, size)

print("The new tuple of subtuples:", new_tuple)