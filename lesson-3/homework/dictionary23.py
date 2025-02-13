def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

dict1 = create_dict_from_input("Enter key-value pairs for the first dictionary (key:value) separated by commas: ")

dict2 = create_dict_from_input("Enter key-value pairs for the second dictionary (key:value) separated by commas: ")

common_keys = set(dict1.keys()) & set(dict2.keys())

if common_keys:
    print(f"The dictionaries have common keys: {common_keys}")
else:
    print("The dictionaries have no common keys.")