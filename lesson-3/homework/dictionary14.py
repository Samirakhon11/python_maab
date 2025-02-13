def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

my_dict = create_dict_from_input("Enter key-value pairs for the dictionary (key:value) separated by commas: ")

value_to_find = input("Enter the value to find the corresponding keys: ")

keys_with_value = [key for key, value in my_dict.items() if value == value_to_find]

if keys_with_value:
    print(f"The keys with the value '{value_to_find}' are: {keys_with_value}")
else:
    print(f"No keys found with the value '{value_to_find}'.")