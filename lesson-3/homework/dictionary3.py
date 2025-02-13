user_input = input("Enter key-value pairs (key:value) separated by commas: ")

my_dict = {}
for pair in user_input.split(','):
    key, value = pair.split(':')
    my_dict[key.strip()] = value.strip()

number_of_keys = len(my_dict)

print(f"The number of keys in the dictionary is: {number_of_keys}")