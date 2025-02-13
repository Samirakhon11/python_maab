def find_max(lst, start, end):
    if start < 0 or end >= len(lst) or start > end:
        return None
    return max(lst[start:end + 1]) 

n = int(input("Enter the number of elements: "))
my_list = []
    
for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    my_list.append(element)

start_index = int(input("Enter the starting index: "))
end_index = int(input("Enter the ending index: "))

result = find_max(my_list, start_index, end_index)

print((f"The largest element is: {result}"))