print("Welcome")

def count_vowels_consonants():
    word = input("Enter a word: ").lower()
    word_set = set(word)
    vowel_count = 0
    consonant_count = 0

    for char in word_set:
        if char in 'aeiou':
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1

    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")

count_vowels_consonants()
