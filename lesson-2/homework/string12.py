def join_words(word_list, separator):
    return separator.join(word_list)

words_input = input("Enter words seperated by a space: ")
to_separate = input("Enter a character to separate: - or ,\n")

words_list_e = words_input.split()
result = join_words(words_list_e, to_separate)

print("New string: ", result)