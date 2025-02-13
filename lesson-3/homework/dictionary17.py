def create_nested_dict_from_input(prompt):
    user_input = input(prompt)
    nested_dict = {}
    for pair in user_input.split(','):
        key, value = pair.split(':')
        key = key.strip()
        value = value.strip()
        if value.startswith('{') and value.endswith('}'):
            inner_dict = eval(value)
            nested_dict[key] = inner_dict
        else:
            nested_dict[key] = value
    return nested_dict

nested_dict = create_nested_dict_from_input("Enter key-value pairs for the nested dictionary (key:value) separated by commas (use {} for inner dictionaries): ")

outer_key = input("Enter the outer key to retrieve from: ")
inner_key = input("Enter the inner key to retrieve the value for: ")

if outer_key in nested_dict and isinstance(nested_dict[outer_key], dict):
    inner_value = nested_dict[outer_key].get(inner_key, "Inner key not found.")
    print(f"The value for '{inner_key}' in '{outer_key}' is: {inner_value}")
else:
    print(f"The outer key '{outer_key}' is not found or it is not a dictionary.")