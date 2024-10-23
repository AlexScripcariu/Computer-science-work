import random

start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))

num = random.randint(start, end)

if num % 2 == 1:
    num += 1

print(num)
