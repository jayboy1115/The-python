def factorial(n):
    result = 1
    for row in range(1, n+1):
        result *= row
    return result

num = int(input("Enter a nonnegative integer: "))
print(f"The factorial of {num} is {factorial(num)}")