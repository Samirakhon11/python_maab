def count_unique_elements(lst):
    return len(set(lst))  

n = int(input("Enter the number of elements: "))
lst = [input(f"Enter element {i + 1}: ") for i in range(n)]

unique_count = count_unique_elements(lst)

print("Number of unique elements:", unique_count)