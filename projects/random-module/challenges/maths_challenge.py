import random

score = 0

for i in range(5):
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    total = num1 + num2

    user_result = int(input(f"Please enter the sum of {num1} and {num2}: "))

    if user_result == total:
        print(f"Correct! ({total})")
        score += 1
    else:
        print(f"Incorrect! Answer: {total}")

print(f"Your total score is: {score}")