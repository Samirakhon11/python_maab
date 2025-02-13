def combine_tuples(tpl1, tpl2):
    return tpl1 + tpl2  

n1 = int(input("Enter the number of elements for the first tuple: "))
tuple1 = tuple(input(f"Enter element {i + 1} for first tuple: ") for i in range(n1))

n2 = int(input("Enter the number of elements for the second tuple: "))
tuple2 = tuple(input(f"Enter element {i + 1} for second tuple: ") for i in range(n2))

combined_tuple = combine_tuples(tuple1, tuple2)

print("Combined tuple:", combined_tuple)