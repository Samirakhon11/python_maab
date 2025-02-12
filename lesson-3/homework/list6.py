def get_first_element(my_list):
    if not my_list or my_list == [""]:  
        return "The list is empty"
    return f"The first element is: {my_list[0]}"

n = input("Enter elements separated by comma (, ): ")
my_list = [item.strip() for item in n.split(',')] 
result = get_first_element(my_list)

print(result) 