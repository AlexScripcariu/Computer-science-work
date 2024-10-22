num = 0

while 10 > num > 20:
    num = int(input("Please enter a number between 10 and 20: "))
    
    if num > 20:
        print("The number is too high!")
    elif num < 10:
        print("The number is too low")

print("Thank you")