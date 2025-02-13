def repeat_elements(tpl, num):
    return tuple(element for element in tpl for _ in range(num))

n = int(input("Enter the number of elements: "))
tpl = tuple(int(input(f"Enter element {i + 1}: ")) for i in range(n))

num = int(input("Enter how many times each element should be repeated: "))
new_tuple = repeat_elements(tpl, num)

print("The new tuple:", new_tuple)