def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

my_dict = create_dict_from_input("Enter key-value pairs for the dictionary (key:value) separated by commas: ")

unique_values = set(my_dict.values())
num_unique_values = len(unique_values)

print(f"The number of unique values in the dictionary is: {num_unique_values}")