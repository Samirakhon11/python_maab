def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

my_dict = create_dict_from_input("Enter key-value pairs for the dictionary (key:value) separated by commas: ")

first_key = next(iter(my_dict))
first_value = my_dict[first_key]

print(f"The first key-value pair is: {first_key}: {first_value}")