print("Welcome")

def count_vowels_consonants():
    word = input("Enter a word: ").lower()
    word_set = set(word)
    vowel_count = 0
    consonant_count = 0

    for char in word_set:
        if char in 'aeiou':
            vowel_count += 1
        else:
            consonant_count += 1

    return f"Vowels: {vowel_count}\nConsonants: {consonant_count}"

print(count_vowels_consonants())

