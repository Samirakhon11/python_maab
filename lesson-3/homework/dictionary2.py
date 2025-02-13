def check_key_in_dict(my_dict, key):
    return key in my_dict

user_input = input("Enter key-value pairs (key:value) separated by commas: ")

my_dict = {}
for pair in user_input.split(','):
    key, value = pair.split(':')
    my_dict[key.strip()] = value.strip()

key_to_check = input("Enter the key to check for presence: ")

exists = check_key_in_dict(my_dict, key_to_check)

if exists:
    print(f"The key '{key_to_check}' is present in the dictionary.")
else:
    print(f"The key '{key_to_check}' is not present in the dictionary.")