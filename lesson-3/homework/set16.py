def filter_even_numbers(my_set):
    return {num for num in my_set if num % 2 == 0}  

n = int(input("Enter the number of elements in the set: "))
my_set = set(int(input(f"Enter element {i + 1}: ")) for i in range(n))

even_set = filter_even_numbers(my_set)

print("Set with only even numbers:", even_set)