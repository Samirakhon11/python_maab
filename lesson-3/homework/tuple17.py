def max_in_subtuple(tpl, start, end):
    subtuple = tpl[start:end]  
    return max(subtuple) if subtuple else None  

n = int(input("Enter the number of elements: "))
tpl = tuple(int(input(f"Enter element {i + 1}: ")) for i in range(n))

start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

result = max_in_subtuple(tpl, start, end)

print("The maximum element in the subtuple:", result)