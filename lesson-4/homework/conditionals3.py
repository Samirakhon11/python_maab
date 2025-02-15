def divide_string(txt):
    vowels = 'aeuio'
    result = []
    count = 0
    i = 0

    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
            if txt[i] in vowels or i > 0 and txt[-2] == '_':
                result.append(txt[i + 1])
                i += 1

            if i < len(txt) - 1:
                result.append('_')

            count = 0

    return ''.join(result)

txt = str(input("Enter a string: "))
result = divide_string(txt)

print(result)