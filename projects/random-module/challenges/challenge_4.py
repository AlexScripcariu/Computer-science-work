import random

continue_loop = True

while continue_loop:
    dice = random.randint(1, 6)
    print(f"You rolled a: {dice}")
    continued = input("Would you like to roll again? (Y/N): ")

    if continued == "Y":
        continue

    break
