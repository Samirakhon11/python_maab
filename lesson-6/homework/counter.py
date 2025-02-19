import os
import string
from collections import Counter

file_name = "sample.txt"

if not os.path.exists(file_name):
    print("File 'sample.txt' not found. Please enter a paragraph to create it:")
    user_text = input("Enter text: ")
    with open(file_name, "w") as file:
        file.write(user_text)
    print("File 'sample.txt' created.")

with open(file_name, "r") as file:
    text = file.read().lower()  

text = text.translate(str.maketrans("", "", string.punctuation))
words = text.split()
word_counts = Counter(words)
total_words = len(words)
top_words = word_counts.most_common(5)

print(f"Total words: {total_words}")
print("Top 5 most common words:")
for word, count in top_words:
    print(f"{word} - {count} {'time' if count == 1 else 'times'}")

with open("word_count_report.txt", "w") as report:
    report.write("Word Count Report\n")
    report.write(f"Total Words: {total_words}\n")
    report.write("Top 5 Words:\n")
    for word, count in top_words:
        report.write(f"{word} - {count}\n")

print("Word count report saved to 'word_count_report.txt'.")
