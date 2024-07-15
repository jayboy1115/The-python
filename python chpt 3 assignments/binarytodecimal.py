def binary_to_decimal():
    binary = int(input("Enter a binary number: "))
    decimal = 0
    power = 1

    while binary != 0:
        digit = binary % 10
        decimal += digit * power
        power *= 2
        binary //= 10

    print("Decimal equivalent:", decimal)

binary_to_decimal()
