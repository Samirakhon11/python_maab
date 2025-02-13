def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

my_dict = create_dict_from_input("Enter key-value pairs for the dictionary (key:value) separated by commas: ")

key_to_retrieve = input("Enter the key to retrieve: ")

if key_to_retrieve in my_dict:
    value = my_dict[key_to_retrieve]
    print(f"The value for the key '{key_to_retrieve}' is: {value}")
else:
    print(f"The key '{key_to_retrieve}' does not exist in the dictionary.")