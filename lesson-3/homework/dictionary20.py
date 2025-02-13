def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

my_dict = create_dict_from_input("Enter key-value pairs for the dictionary (key:value) separated by commas: ")

sorted_dict = dict(sorted(my_dict.items()))

print("The dictionary sorted by keys is:")
for key in sorted_dict:
    print(f"{key}: {sorted_dict[key]}")