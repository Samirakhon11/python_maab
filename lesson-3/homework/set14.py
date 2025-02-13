def find_max(my_set):
    if my_set:  
        return max(my_set) 
    else:
        return "The set is empty."

n = int(input("Enter the number of elements in the set: "))
my_set = set(int(input(f"Enter element {i + 1}: ")) for i in range(n))

max_element = find_max(my_set)
print("The maximum element:", max_element)