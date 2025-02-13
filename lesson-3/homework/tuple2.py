def find_max(tpl):
    return max(tpl) 

n = int(input("Enter the number of elements: "))
elements = tuple(int(input(f"Enter element {i + 1}: ")) for i in range(n))

print(f"The largest element is: {find_max(elements)}")
