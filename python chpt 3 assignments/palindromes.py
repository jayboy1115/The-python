print("WELCOME TO JOHNSON WORLD")

num = int(input("Enter a five-digit integer: "))

a = num // 10000
b = (num // 1000) % 10
c = (num // 100) % 10
d = (num // 10) % 10
e = num % 10

if a == e and b == d:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
