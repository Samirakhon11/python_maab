def create_tuple(start, end):
    return tuple(range(start, end + 1))

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

number_tuple = create_tuple(start, end)

print("The generated tuple:", number_tuple)