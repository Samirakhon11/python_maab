def create_set_in_range(start, end):
    return set(range(start, end + 1))  

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

num_set = create_set_in_range(start, end)

print("Set of numbers in the given range:", num_set)