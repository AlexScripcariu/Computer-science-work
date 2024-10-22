#Task 1
again = "yes"

while again == "yes":
    print("Hello")
    again = input("Do you want to loop again?: ").lower()

#Task 2
total = 0

while total < 100:
    num = int(input("Enter a number: "))
    total += num

print(f"The total is {total}")
