def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

dict1 = create_dict_from_input("Enter key-value pairs for the first dictionary (key:value) separated by commas: ")
dict2 = create_dict_from_input("Enter key-value pairs for the second dictionary (key:value) separated by commas: ")

combined_dict = {**dict1, **dict2}

print("The combined dictionary is:", combined_dict)