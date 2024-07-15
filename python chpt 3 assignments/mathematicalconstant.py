def calculate_pi(n):
    pi = 0.0
    for num in range(n):
        pi += ((-1) ** num) / (2 * num + 1)
    pi *= 4
    return pi

print("Number of terms | Approximation of π")
print("-------------|--------------------")
for num in range(1, 100):
    pi = calculate_pi(num)
    print(f"{num:>13} | {pi:.6f}")
    if pi >= 3.14 and num == 1:
        print(f"First 3.14: {num} terms")
    elif pi >= 3.141 and num == 2:
        print(f"First 3.141: {num} terms")
    elif pi >= 3.1415 and num == 3:
        print(f"First 3.1415: {num} terms")
    elif pi >= 3.14159 and num == 4:
        print(f"First 3.14159: {num} terms")
        break

