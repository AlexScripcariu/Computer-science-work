import random

choices = ["h", "t"]
coin_flip = random.choice(choices)

user_choice = input("Please choose heads or tails: ").lower()

picked = "heads" if coin_flip == "h" else "tails"

if user_choice == picked:
    print("You win")
else:
    print("Bad luck")

print(f"the computer selected {picked}")
