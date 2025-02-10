def creat_acronym(sentence):
    words = sentence.split()
    acronym = ''.join(word[0].upper() for word in words)
    
    return acronym

sentence = input("Enter a sentence: \n")
acronym = creat_acronym(sentence)

print("Acronym for the sentence is: ", acronym)