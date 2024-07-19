import random

def arithmetic_quiz():
    score = 0
    attempts = 10

    while attempts > 0:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2

        user_answer = int(input(f"What is {num1} + {num2}? ({attempts} attempts left): "))

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {answer}.")

        attempts -= 1

    print(f"Your final score is {score} out of 10.")

arithmetic_quiz()