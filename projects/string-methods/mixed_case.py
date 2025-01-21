user_string = input("Please enter a 10 character long string: ")

while len(user_string) != 10: 
    user_string = input("Please enter a 10 character long string: ")

user_string = user_string[:5].lower() + user_string[5:].upper()

print(user_string)