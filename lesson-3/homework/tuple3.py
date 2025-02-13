def find_min(tpl):
    return min(tpl) 

n = int(input("Enter the number of elements: "))
elements = tuple(int(input(f"Enter element {i + 1}: ")) for i in range(n))

print(f"The smallest element is: {find_min(elements)}")