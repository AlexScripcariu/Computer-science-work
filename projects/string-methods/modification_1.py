password = input("Please enter a password: ")

while not(6 <= len(password) <= 12) or not(password.isalpha() or password.isdigit()):
    password = input("Please enter a password: ")

print("password accepted")