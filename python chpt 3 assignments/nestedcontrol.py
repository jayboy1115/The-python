largest = float('-inf')
second_largest = float('-inf')

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))

    if num > largest:
        second_largest = largest
        largest = num
    
    elif num > second_largest:
        second_largest = num

print(f"The two largest values are {largest} and {second_largest}")

