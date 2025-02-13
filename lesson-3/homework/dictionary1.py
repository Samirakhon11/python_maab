def get_value_from_dict(my_dict, key):
    return my_dict.get(key, "Key does not exist.")

user_input = input("Enter key-value pairs (key:value) separated by commas: ")

my_dict = {}
for pair in user_input.split(','):
    key, value = pair.split(':')
    my_dict[key.strip()] = value.strip()

key_to_retrieve = input("Enter the key to retrieve its value: ")

result = get_value_from_dict(my_dict, key_to_retrieve)

print(result)
