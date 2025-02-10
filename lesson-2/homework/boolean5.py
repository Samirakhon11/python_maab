def check_length(str1, str2):
    return len(str1) == len(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = check_length(string1, string2)

if result:
    print("The strings have the same length.")
else:
    print("The strings do not have the same length.")