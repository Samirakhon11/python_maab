def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

keys_input = input("Enter keys separated by commas: ")
values_input = input("Enter values separated by commas: ")

keys_list = [key.strip() for key in keys_input.split(',')]
values_list = [value.strip() for value in values_input.split(',')]

if len(keys_list) != len(values_list):
    print("Error: The number of keys and values must be the same.")
else:
    paired_dict = create_dict_from_lists(keys_list, values_list)
    
    print("The resulting dictionary is:", paired_dict)