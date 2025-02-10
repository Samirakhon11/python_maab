sentence = input("Enter a sentence: \n")
words = sentence.split()
start = words[0]
end = words[len(words) - 1]

print("Input:", sentence)
print("Starts with \"", start, "\"")
print("Ends with \"", end, "\"")