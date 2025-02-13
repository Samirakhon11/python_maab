def create_list(start, end):
    return list[range(start, end + 1)]

start = int(input("Enter a starting number: "))
end = int(input("Emter an ending number: "))

print(f"List: {create_list(start, end)}")