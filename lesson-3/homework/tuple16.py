def is_sorted(tpl):
    return tpl == tuple(sorted(tpl)) 

n = int(input("Enter the number of elements: "))
tpl = tuple(int(input(f"Enter element {i + 1}: ")) for i in range(n))

result = is_sorted(tpl)

print("Is the tuple sorted in ascending order?", result)