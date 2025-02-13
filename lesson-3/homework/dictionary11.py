def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

my_dict = create_dict_from_input("Enter key-value pairs for the dictionary (key:value) separated by commas: ")

key_to_update = input("Enter the key to update: ")
new_value = input("Enter the new value: ")

if key_to_update in my_dict:
    my_dict[key_to_update] = new_value
    print(f"The value for the key '{key_to_update}' has been updated to: {new_value}")
else:
    print(f"The key '{key_to_update}' does not exist in the dictionary.")

print("The updated dictionary is:", my_dict)