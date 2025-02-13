def reverse_tuple(tpl):
    return tpl[::-1]

n = int(input("Enter the number of elements: "))
tpl = tuple(input(f"Enter element {i + 1}: ") for i in range(n))

reversed_tpl = reverse_tuple(tpl)

print("Reversed: ", reversed_tpl)