# asks the user for a number
user_number = int(input("Please enter a whole number: "))
user_number_remainder = user_number % 2 # checks to see if the number is even

# prints out the result
if user_number == 0:
    print("You entered an even number!")
else:
    print("You entered an odd nubmer!")
