def divide_string(txt):
    vowels = 'aeiou'
    result = []
    count = 0
    seen_chars = set()  # To track characters that have already ended a segment

    i = 0
    while i < len(txt):
        # Add the current character to the result
        result.append(txt[i])
        count += 1

        # Check the conditions for adding an underscore
        if count == 3:
            if txt[i] not in vowels and txt[i] not in seen_chars:
                result.append('_')
                seen_chars.add(txt[i])  # Mark this character as seen
            count = 0  # Reset count after adding underscore (if applicable)

        i += 1  # Move to the next character

    return ''.join(result)

# Test the function
txt = input("Enter a string: ")
result = divide_string(txt)
print(result)