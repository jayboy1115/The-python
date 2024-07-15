import math

def estimate_e(n):
    e = 0.0
    for i in range(n):
        e += 1 / math.factorial(i)
    return e

print("Estimated value of e:", estimate_e(10))