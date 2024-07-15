score = int(input("enter your score "))

total = 0
counter = 0

while score != -6:
	counter += 1
	total += score
	score = int(input("enter your score "))
averagescore = total / 2
print(averagescore)