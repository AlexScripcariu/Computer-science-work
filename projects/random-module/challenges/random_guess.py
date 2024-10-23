import random

compnum = random.randint(1, 100)
guesses = 0
winner = False
while winner == False:
    num = int(input("Enter a number between 1-100: "))
    guesses += 1
    if num < 1 and num > 100:
        print("Out of range")
        continue
    elif num == compnum:
        print("You win")
        winner = True
        continue

    print("Wrong answer, try again")

print("The number of guesses=", guesses)