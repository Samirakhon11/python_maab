def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

my_dict = create_dict_from_input("Enter key-value pairs for the dictionary (key:value) separated by commas: ")
threshold = float(input("Enter a threshold value: "))
filtered_dict = {key: value for key, value in my_dict.items() if isinstance(value, (int, float)) and value > threshold}

print("The filtered dictionary is:")
for key in filtered_dict:
    print(f"{key}: {filtered_dict[key]}")