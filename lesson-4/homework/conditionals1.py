n1 = int(input("Enter the number of elements for the first list: "))
lst1 = []

for i in range(n1):
    element = input(f"Enter element {i + 1}: ")
    lst1.append(element)

n2 = int(input("Enter the number of elements for the second list: "))
lst2 = []

for i in range(n2):
    element = input(f"Enter element {i + 1}: ")
    lst2.append(element)

if not lst1 or not lst2:
    print("The lists are empty!")
else:
    set1 = set(lst1)
    set2 = set(lst2)
    lst_final = list(set1.symmetric_difference(set2))
 
print("New list: ", lst_final) 