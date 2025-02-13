import random

def generate_random_set(count, start, end):
    count = min(count, end - start + 1)
    return set(random.sample(range(start, end + 1), count))

count = int(input("Enter the number of random integers: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

random_set = generate_random_set(count, start, end)

print("Generated random set:", random_set)