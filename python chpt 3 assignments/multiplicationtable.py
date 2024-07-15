def multiplication_table(num):
    for row in range(1, 11):
        print(f"{num}x{row}={num*row}")

num = int(input("Enter a number: "))
multiplication_table(num)

