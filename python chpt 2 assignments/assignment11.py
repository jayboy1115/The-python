print('welcome')

num = int(input("Enter a five-digit integer: "))


digit1 = num // 10000
digit2 = (num // 1000) % 10
digit3 = (num // 100) % 10
digit4 = (num // 10) % 10
digit5 = num % 10


print(digit1, digit2, digit3, digit4, digit5, sep='   ')

