num_one = int(input("Please enter a number: "))
num_two = int(input("Please enter another number: "))

total = num_one + num_two

keep_looping = input("Do you want to continue Y/N: ")

while keep_looping == "Y":
    temp = int(input("Enter another number: "))
    total += temp

print(f"The total is {total}")
