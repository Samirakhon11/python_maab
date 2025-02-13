def create_dict_from_tuple(pairs):
    return dict(pairs)

key_value_pairs = (('name', 'Alice'), ('age', 30), ('city', 'New York'))

my_dict = create_dict_from_tuple(key_value_pairs)

print("The created dictionary is:")
print(my_dict)