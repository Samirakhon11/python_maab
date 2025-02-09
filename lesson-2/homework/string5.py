def countVowelsConsonants(word):
    vowels = 'aeuioAEUIO'
    consonants = 'qwrtyplkjhgfdszxcvbnmQWRTYPLKJHGFDSZXCVBNM'
    vowel_count = 0
    consonant_count = 0

    for letter in word:
        if letter in vowels:
            vowel_count += 1
        elif letter in consonants:
            consonant_count += 1
    return vowel_count, consonant_count

word = input("Enter a string: ")
vowels, consonants = countVowelsConsonants(word)

print("Number of vowels:", {vowels})
print("Number of consonants:", {consonants})