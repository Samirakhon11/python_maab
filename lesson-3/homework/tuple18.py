def min_in_subtuple(tpl, start, end):
    subtuple = tpl[start:end]
    return min(subtuple) if subtuple else None

n = int(input("Enter the number of elements: "))
tpl = tuple(int(input(f"Enter element {i + 1}: ")) for i in range(n))

start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

result = min_in_subtuple(tpl, start, end)

print("The minimum element in the subtuple:", result)