from random import randint

game = randint(1,1000)
total_trials = 0

while True:
    user = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
    total_trials += 1

    if user == -1:
        break

    if user == game:
        print(f"Congratulations! You guessed the number in {total_trials} trials.")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            game = randint(1,1000)
            total_trials = 0
        else:
            break
    elif user > game:
        print("Your guess is too high. Try again!")
    else:
        print("Your guess is too low. Try again!")

