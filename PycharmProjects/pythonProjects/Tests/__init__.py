from Tests.charcounter import CharCounter

def main():
    counter_obj = CharCounter()
    while True:
        word = input("Enter a word: ")
        if word.replace(" ", "") == "":
            print("Character Counter:")
            print({})
            break
        elif word.replace(" ", "").isalpha():
            counter = char_counter(word.replace(" ", ""))
            print("Character Counter:")
            print(counter)
            break
        else:
            print("Error: Input should only contain letters. Please try again.")

if __name__ == "__main__":
    main()















