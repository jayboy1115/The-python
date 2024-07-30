# Prompt for sentence from user
# Initialize letter_counter to 0
# Initialize digit_counter to 0
# Iterate over each character in the sentence
# Check if the character is a letter
# Increment letter_counter
# Check if the character is a digit
# Increment digit_counter
# Print the results


sentence = input("Enter a sentence: ")
letter_counter = 0
digit_counter = 0

for char in sentence:
    if char.isalpha():
        letter_counter += 1
    
    elif char.isdigit():
        digit_counter += 1

print("LETTERS", letter_counter)
print("DIGITS", digit_counter)

