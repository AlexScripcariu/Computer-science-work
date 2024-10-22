guesses = 0
comp_num = 50

user_guess = int(input("Please guess a number: "))
guesses += 1

while user_guess != comp_num:
    if user_guess > comp_num:
        print("That number is too high!")
    else:
        print("That number is too low!")
    
    user_guess = int(input("Please guess a number: "))
    guesses += 1

print(f"Guesses: {guesses}")