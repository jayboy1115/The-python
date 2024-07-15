print("welcome")

grade = int (input("enter a score "))

if grade >= 75 and grade < 100:
	print("your grade is A ")
elif grade >= 65 and grade < 75:
	print("your grade is B ")
elif grade >= 50 and grade < 65:
	print("your grade is c ")
elif grade >= 40 and grade < 50:
	print("your grade is D ")
else:
	print("your grade is F ")    