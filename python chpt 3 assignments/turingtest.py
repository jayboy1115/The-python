print("WELCOME TO JOHNSON MEDICAL DIAGNOSIS")

print("What is your problem?")
user_input = input()  

print("Have you had this problem before (yes or no)?")
user_input = input()

if user_input.lower() == "yes":
    print("Well, you have it again.")
elif user_input.lower() == "no":
    print("Well, you have it now.")
else:
    print("Invalid input. Please answer yes or no.")

