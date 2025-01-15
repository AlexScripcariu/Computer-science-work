password = "cheese123"

while True:
    input_passowrd = input("Please enter your password: ")

    if input_passowrd != password:
        print("Password do not match. Error code 6.")
        continue

    print("Number accepted!")
    break