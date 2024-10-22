num = int(input("Please enter a number (be careful!): "))

while num:
    print(f"""There are {num} green bottles hanging on the wall, {num} green bottles hanging on the \
wall and if 1 green bottle should accidentally fall""")
    
    next_bottles = int(input("how many green bottles will be hanging on the wall?: "))

    if next_bottles == num - 1:
        num -= 1
        continue

    print("Incorrect, try again...")
