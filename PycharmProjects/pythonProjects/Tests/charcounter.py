def char_counter(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    if any(char.isdigit() for char in word):
        raise ValueError("Input must not contain numbers")
    counter = {}
    for char in word:
        if char != ' ':
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    return counter

