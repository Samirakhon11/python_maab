def remove_first_occurrence(tpl, element):
    lst = list(tpl)
    if element in lst:
        lst.remove(element)
    return tpl(lst)

n = int(input("Enter the number of elements: "))
tpl = tuple(int(input(f"Enter element {i + 1}: ")) for i in range(n))

element = int(input("Enter the element to remove: "))
new_tuple = remove_first_occurrence(tpl, element)

print("The new tuple:", new_tuple) 