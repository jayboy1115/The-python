def add_ce(word):
    middle_index = len(word) // 2
    if len(word) % 2 == 0:
        return word + 'ce'
    else:
        return word[:middle_index] + 'ce' + word[middle_index:]
