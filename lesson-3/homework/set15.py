def find_min(my_set):
    if my_set:  
        return min(my_set)  
    else:
        return "The set is empty."

n = int(input("Enter the number of elements in the set: "))
my_set = set(int(input(f"Enter element {i + 1}: ")) for i in range(n))

min_element = find_min(my_set)
print("The minimum element:", min_element)