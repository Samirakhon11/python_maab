user_input = input("Enter key-value pairs (key:value) separated by commas: ")

my_dict = {}
for pair in user_input.split(','):
    key, value = pair.split(':')
    my_dict[key.strip()] = value.strip()

keys_list = list(my_dict.keys())

print("The list of keys in the dictionary is:", keys_list)