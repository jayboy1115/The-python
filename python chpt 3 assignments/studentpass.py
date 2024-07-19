pass_count = 0

for counter in range(15):
    score = int(input(f"Enter score for student {counter+1}: "))
    if score >= 45:
        pass_count += 1

print(f"Number of students who passed: {pass_count}")
print(f"Number of students who failed: {15 - pass_count}")

