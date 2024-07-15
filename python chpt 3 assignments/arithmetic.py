print("WELCOME TO JOHNSON WORLD")

numbers = []
for row in range(4):
    num = int(input(f"Enter number {row+1}: "))
    numbers.append(num)

sum = sum(numbers)
average = sum / 4
product = 1
for num in numbers:
    product *= num
smallest = min(numbers)
largest = max(numbers)

print(f"Sum: {sum}")
print(f"Average: {average}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")

