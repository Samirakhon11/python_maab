from collections import defaultdict

# Function to create a defaultdict with a specified default value
def create_default_dict(default_value):
    return defaultdict(lambda: default_value)

default_value = input("Enter the default value for missing keys: ")

my_dict = create_default_dict(default_value)

while True:
    key = input("Enter a key to add (or type 'exit' to finish): ")
    if key.lower() == 'exit':
        break
    value = input(f"Enter a value for '{key}': ")
    my_dict[key] = value

print("The resulting dictionary is:")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

missing_key = input("Enter a key to check for its value (it may be missing): ")
print(f"The value for '{missing_key}' is: {my_dict[missing_key]}")