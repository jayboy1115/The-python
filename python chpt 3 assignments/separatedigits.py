print("WELCOME TO JOHNSON WORLD")

num = int(input("Enter a five-digit integer: "))

for _ in range(5):
    digit = num % 10
    print(digit)
    num = num // 10
