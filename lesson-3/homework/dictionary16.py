def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

my_dict = create_dict_from_input("Enter key-value pairs for the dictionary (key:value) separated by commas: ")

has_nested_dict = any(isinstance(value, dict) for value in my_dict.values())

if has_nested_dict:
    print("There is at least one value that is a dictionary.")
else:
    print("There are no values that are dictionaries.")