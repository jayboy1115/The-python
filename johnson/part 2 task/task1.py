

for number in range(1000, 3000):
    if number % 2 == 0:
        first_number = [int(digit) for digit in str(number)]
        if all(counter % 2 == 0 for counter in first_number):
            print(number, end=", ")

