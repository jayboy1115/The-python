print("WELCOME TO JOHNSON WORLD")

passes = 0
failures = 0

while True:
    number1 = int(input('Enter first integer (1 or 2): '))
    if number1 in [1, 2]:
        passes += 1
        break
    else:
        failures += 1
        print('Invalid input. Please enter 1 or 2.')

while True:
    number2 = int(input('Enter second integer (1 or 2): '))
    if number2 in [1, 2]:
        passes += 1
        break
    else:
        failures += 1
        print('Invalid input. Please enter 1 or 2.')

total = number1 + number2
print('The sum of', number1, 'and', number2, 'is', total)
print('Number of passes:', passes)
print('Number of failures:', failures)

