def check_sublist_exists(main_list, sublist):
    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i + len(sublist)] == sublist:
            return True
    return False

user_main_list = input("Enter the main list of elements (separated by commas): ")
main_list = [item.strip() for item in user_main_list.split(',')]

user_sublist = input("Enter the sublist to check (separated by commas): ")
sublist = [item.strip() for item in user_sublist.split(',')]

exists = check_sublist_exists(main_list, sublist)

if exists:
    print("The sublist exists within the main list.")
else:
    print("The sublist does not exist within the main list.")