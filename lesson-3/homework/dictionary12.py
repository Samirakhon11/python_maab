def create_dict_from_input(prompt):
    user_input = input(prompt)
    new_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        new_dict[key.strip()] = value.strip()
    return new_dict

my_dict = create_dict_from_input("Enter key-value pairs for the dictionary (key:value) separated by commas: ")

value_to_count = input("Enter the value to count: ")

count = sum(1 for value in my_dict.values() if value == value_to_count)

print(f"The value '{value_to_count}' appears {count} times in the dictionary.")