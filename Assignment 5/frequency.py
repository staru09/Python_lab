def count_vowels_consonants(filename):
    vowels = "aeiouAEIOU"
    with open(filename, 'r') as file:
        text = file.read()
        vowel_count = sum(1 for char in text if char in vowels)
        consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

filename = input("Enter file name: ")
vowels, consonants = count_vowels_consonants(filename)
print("Vowels:", vowels)
print("Consonants:", consonants)
