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
    lst_final = [i for i in lst1 if i not in lst2] + [j for j in lst2 if j not in lst1]
 
print("New list: ", lst_final) 