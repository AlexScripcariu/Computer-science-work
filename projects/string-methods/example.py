password = input("Please enter a password: ")

while password.isalpha() or password.isdigit():
    password = input("Please enter a password: ")

print("password accepted")