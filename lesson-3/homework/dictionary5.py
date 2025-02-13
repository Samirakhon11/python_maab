user_input = input("Enter key-value pairs (key:value) separated by commas: ")

my_dict = {}
for pair in user_input.split(','):
    key, value = pair.split(':')
    my_dict[key.strip()] = value.strip()

values_list = list(my_dict.values())

print("The list of values in the dictionary is:", values_list)