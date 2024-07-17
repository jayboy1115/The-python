from random import randint
game = randint(1,1000)
user = int(input("enter any number to start the game or -1 to exit \n"))

while user != -1:
	user = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))

	if user == game:
	      	print("Congratulations. You guessed the number!")
	elif user > game:
		print("your guess is too high try again")
	
	else:
		print("your guess is too low try again")

	