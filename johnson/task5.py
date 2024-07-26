# prompt the user to enter an integer between 0 and 100 
# Initialize the sum of digits to be 0 
# Extract each digit and add it to the sum
# print the sum of digits


num = int(input("Enter an integer between 0 and 1000: "))

sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10

print(f"The sum of the digits is: {sum_of_digits}")

  