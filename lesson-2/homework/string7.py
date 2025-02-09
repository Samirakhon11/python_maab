sentence = input("Enter a sentence: ")
to_change = input("Enter a word which should be changed: ")
to_replace = input("Enter a word to replace it: ")

new_sentence = sentence.replace(to_change, to_replace)

print("New sentence:\n", new_sentence)