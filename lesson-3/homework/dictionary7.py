def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

my_dict = create_dict_from_input("Enter key-value pairs for the dictionary (key:value) separated by commas: ")

key_to_remove = input("Enter the key to remove: ")

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"The key '{key_to_remove}' has been removed.")
else:
    print(f"The key '{key_to_remove}' does not exist in the dictionary.")

print("The updated dictionary is:", my_dict)