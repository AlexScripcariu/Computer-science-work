# asks the user for a 3 letter animal
animal = input("Please enter a three letter animal: ")

# keeps looping until animal length = 3 (length check)
while len(animal) != 3:
    animal = input("Please enter a three letter animal: ")


# this dictionary stores the animal and their sound
animal_sounds = {
    "cat": "meow",
    "dog": "woof",
    "cow": "moo",
    "fox": "howl"
}

# attempts to retrieve the sound the animal is making
try: 
    print(animal_sounds[animal])
except KeyError:    # if animal is not found, then it will print out a message
    print("Animal not found!")