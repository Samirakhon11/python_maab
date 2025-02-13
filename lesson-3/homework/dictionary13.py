def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

original_dict = create_dict_from_input("Enter key-value pairs for the dictionary (key:value) separated by commas: ")

swapped_dict = {value: key for key, value in original_dict.items()}

print("Original dictionary:", original_dict)
print("Swapped dictionary:", swapped_dict)